import os
import random
import time
import threading
import pygame
import mysql.connector
from flask import Flask, render_template, jsonify


app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'qwerty_123',
    'database': 'vericall'
}
def load_model(model_path):
    return joblib.load(model_path)

def extract_features(audio_file, n_mfcc=40, hop_length=512, n_fft=2048):
    y, sr = librosa.load(audio_file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length, n_fft=n_fft)
    return mfccs.T

def detect_deepfake_audio(audio_file, model):
    features = extract_features(audio_file)
    prediction = model.predict(features)
    return "Fake" if prediction[0] == 0 else "Real"
# Path to the folder containing audio files
AUDIOS_FOLDER = "audios"

# Path to the ringtone file
RINGTONE_FILE_PATH = 'ringtone.mp3'

# Initialize pygame mixer
pygame.mixer.init()

# Global variable to store the receiver number
receiver_number = None

# Function to establish database connection
def connect_to_database():
    return mysql.connector.connect(**db_config)

# Function to fetch a random phone number from the database
def get_random_phone_number():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT number FROM phone_numbers ORDER BY RAND() LIMIT 1")
    phone_number = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return phone_number

# Function to play the ringtone
def play_ringtone():
    pygame.mixer.music.load(RINGTONE_FILE_PATH)
    pygame.mixer.music.play()

# Function to stop the ringtone
def stop_ringtone():
    pygame.mixer.music.stop()

def load_model(model_path):
    return joblib.load(model_path)

def extract_features(audio_file, n_mfcc=40, hop_length=512, n_fft=2048):
    y, sr = librosa.load(audio_file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length, n_fft=n_fft)
    return mfccs.T

def detect_deepfake_audio(audio_file, model):
    features = extract_features(audio_file)
    prediction = model.predict(features)
    return "Fake" if prediction[0] == 0 else "Real"

# Function to play a random audio file from the audios folder and return its duration
def play_random_audio():
    folder_list = [folder for folder in os.listdir(AUDIOS_FOLDER) if os.path.isdir(os.path.join(AUDIOS_FOLDER, folder))]
    chosen_folder = random.choice(folder_list)
    if chosen_folder == 'real':
        print("Real")
    else:
        print("Fake")
    audio_files = [file for file in os.listdir(os.path.join(AUDIOS_FOLDER, chosen_folder)) if file.endswith('.wav')]
    if not audio_files:
        print("No audio files found in the chosen folder.")
        return None, None, None
    chosen_audio = random.choice(audio_files)
    audio_file_path = os.path.join(AUDIOS_FOLDER, chosen_folder, chosen_audio)
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()
    audio_length = pygame.mixer.Sound(audio_file_path).get_length()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    if chosen_folder == 'fake':
        print("Audio is deepfaked.")
        audio_type = "Fake"
    else:
        print("Audio is original.")
        audio_type = "Real"
    return audio_file_path, audio_type, audio_length

# Function to fetch contact name based on the phone number
def get_contact_name(phone_number):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM contacts WHERE number = %s", (phone_number,))
    contact_name = cursor.fetchone()
    cursor.close()
    conn.close()
    return contact_name[0] if contact_name else "Unknown"

# Function to record call history
def record_call_history(caller_number, receiver_number, call_type, call_duration, deepfake, contact_name):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO call_history (caller_number, receiver_number, call_type, call_duration, deepfake, contact_name) VALUES (%s, %s, %s, %s, %s, %s)", (caller_number, receiver_number, call_type, call_duration, deepfake, contact_name))
    conn.commit()
    cursor.close()
    conn.close()

# Function to open receive_call.html after random seconds
def open_receive_call():
    global receiver_number
    time.sleep(random.randint(10, 15))
    receiver_number = get_random_phone_number()  # Set the global receiver_number
    return render_template("receive_call.html", phone_number=receiver_number)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/make_call")
def make_call():
    phone_number = get_random_phone_number()
    return render_template("make_call.html", phone_number=phone_number)

@app.route("/receive_call")
def receive_call():
    global receiver_number
    receiver_number = None  # Reset receiver number to fetch a new random number
    if receiver_number is None:  # If receiver number is not set, fetch a new one
        receiver_number = get_random_phone_number()
    contact_name = get_contact_name(receiver_number)
    is_known_contact = contact_name != "Unknown"
    play_ringtone()
    return render_template("receive_call.html", phone_number=receiver_number, contact_name=contact_name, is_known_contact=is_known_contact)



@app.route("/call_history")
def call_history():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, caller_number, receiver_number, call_type, call_duration, deepfake, contact_name, call_timestamp AS timestamp FROM call_history")  # Use call_timestamp and alias it as timestamp
    call_history = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("call_history.html", call_history=call_history)



@app.route("/pick", methods=["POST"])
def pick():
    global receiver_number
    stop_ringtone()  # Stop the ringtone
    audio_file_path, audio_type, audio_duration = play_random_audio()  # Play random audio
    # Dummy values for demonstration
    caller_number = '7416622564'
    if receiver_number is None:  # If receiver number is not set, fetch a new one
        receiver_number = get_random_phone_number()
    call_type = 'incoming'
    call_duration = time.strftime("%H:%M:%S", time.gmtime(audio_duration))  # Convert audio duration to HH:MM:SS format
    deepfake = True if audio_type == "Fake" else False
    contact_name = get_contact_name(receiver_number)
    record_call_history(caller_number, receiver_number, call_type, call_duration, deepfake, contact_name)
    return jsonify({"success": True, "message": "Call picked", "audio_type": audio_type})

@app.route("/hang", methods=["POST"])
def hang():
    stop_ringtone()  # Stop the ringtone
    return jsonify({"success": True, "message": "Call hung up"})

if __name__ == "__main__":
    model_path = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\aiaudio\random_forest_model.joblib"
    audio_file = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\data\fake\LJ001-0001_gen.wav"
    app.run(debug=True)



