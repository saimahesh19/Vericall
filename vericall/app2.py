import os
import random
from flask import Flask, render_template, jsonify
import threading
import vlc
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'qwerty_123',
    'database': 'vericall'
}

# Path to the folder containing audio files
AUDIOS_FOLDER =  r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\audios"

# Path to the ringtone file
RINGTONE_FILE_PATH = r'C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\ringtone.mp3'
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
# Global variable to store the player instance
player = None

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

# Function to play audio
def play_audio(audio_file_path):
    global player
    player = vlc.MediaPlayer(audio_file_path)
    player.play()
    # Looping the audio until the application is terminated
    while True:
        if player.get_state() == vlc.State.Ended:
            player.play()

# Thread for playing audio
def start_audio_thread(audio_file_path):
    audio_thread = threading.Thread(target=play_audio, args=(audio_file_path,))
    audio_thread.daemon = True
    audio_thread.start()

# Function to play a random audio file from the audios folder
def play_random_audio():
    audio_files = os.listdir(AUDIOS_FOLDER)
    if audio_files:
        random_audio_file = random.choice(audio_files)
        audio_file_path = os.path.join(AUDIOS_FOLDER, random_audio_file)
        start_audio_thread(audio_file_path)

# Function to play the ringtone
def play_ringtone():
    ringtone_thread = threading.Thread(target=start_audio_thread, args=(RINGTONE_FILE_PATH,))
    ringtone_thread.daemon = True
    ringtone_thread.start()

@app.route("/")
def index():
    # Play the ringtone when the page is loaded
    play_ringtone()
    # Fetch a random phone number from the database
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT number FROM phone_numbers ORDER BY RAND() LIMIT 1")
    result = cursor.fetchone()
    phone_number = result[0] if result else "Unknown"
    cursor.close()
    conn.close()
    return render_template("index.html", phone_number=phone_number)


@app.route("/pick", methods=["POST"])
def pick():
    global player
    if player:
        player.pause()
    # Start playing a random audio file when the call is picked up
    play_random_audio()
    # Logic to handle when the call is picked up
    return jsonify({"success": True, "message": "Call picked"})

@app.route("/hang", methods=["POST"])
def hang():
    global player
    if player:
        player.pause()
    # Logic to handle when the call is hung up
    return jsonify({"success": True, "message": "Call hung up"})

if __name__ == "__main__":
    app.run(debug=True)

 
# import os
# import random
# from flask import Flask, render_template, jsonify, request
# import threading
# import vlc
# import mysql.connector
# import joblib
# import librosa
# import numpy as np

# app = Flask(__name__)

# # Database connection configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'qwerty_123',
#     'database': 'vericall'
# }

# # Path to the folder containing audio files
# AUDIOS_FOLDER = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\audios"

# # Path to the ringtone file
# RINGTONE_FILE_PATH = r'C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\ringtone.mp3'

# # Path to the model for deepfake audio detection
# MODEL_PATH = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\aiaudio\random_forest_model.joblib"

# # Global variables
# player = None
# model = None

# # Function to establish database connection
# def connect_to_database():
#     return mysql.connector.connect(**db_config)

# # Function to fetch a random phone number from the database
# def get_random_phone_number():
#     conn = connect_to_database()
#     cursor = conn.cursor()
#     cursor.execute("SELECT number FROM phone_numbers ORDER BY RAND() LIMIT 1")
#     phone_number = cursor.fetchone()[0]
#     cursor.close()
#     conn.close()
#     return phone_number

# # Function to play audio
# def play_audio(audio_file_path):
#     global player
#     player = vlc.MediaPlayer(audio_file_path)
#     player.play()
#     # Looping the audio until the application is terminated
#     while True:
#         if player.get_state() == vlc.State.Ended:
#             player.play()

# # Thread for playing audio
# def start_audio_thread(audio_file_path):
#     audio_thread = threading.Thread(target=play_audio, args=(audio_file_path,))
#     audio_thread.daemon = True
#     audio_thread.start()

# # Function to play a random audio file from the audios folder
# def play_random_audio():
#     audio_files = os.listdir(AUDIOS_FOLDER)
#     if audio_files:
#         random_audio_file = random.choice(audio_files)
#         audio_file_path = os.path.join(AUDIOS_FOLDER, random_audio_file)
#         start_audio_thread(audio_file_path)
#         return audio_file_path  # Return the path of the played audio file
#     return None

# # Function to play the ringtone
# def play_ringtone():
#     ringtone_thread = threading.Thread(target=start_audio_thread, args=(RINGTONE_FILE_PATH,))
#     ringtone_thread.daemon = True
#     ringtone_thread.start()

# # Load deepfake audio detection model
# def load_deepfake_model():
#     global model
#     model = joblib.load(MODEL_PATH)

# # Function to extract features from audio file
# def extract_features(audio_file, n_mfcc=40, hop_length=512, n_fft=2048):
#     y, sr = librosa.load(audio_file)
#     mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length, n_fft=n_fft)
#     return mfccs.T

# # Function to detect deepfake audio
# def detect_deepfake_audio(audio_file):
#     features = extract_features(audio_file)
#     prediction = model.predict(features)
#     return "Fake" if prediction[0] == 0 else "Real"

# # Route for index page
# @app.route("/")
# def index():
#     # Play the ringtone when the page is loaded
#     play_ringtone()
#     # Fetch a random phone number from the database
#     conn = connect_to_database()
#     cursor = conn.cursor()
#     cursor.execute("SELECT number FROM phone_numbers ORDER BY RAND() LIMIT 1")
#     result = cursor.fetchone()
#     phone_number = result[0] if result else "Unknown"
#     cursor.close()
#     conn.close()
#     return render_template("index.html", phone_number=phone_number)

# # Route for picking up the call
# @app.route("/pick", methods=["POST"])
# def pick():
#     global player
#     if player:
#         player.pause()
    
#     # Play a random audio file and get its path
#     audio_file_path = play_random_audio()
    
#     if audio_file_path:
#         # Detect if the audio is deepfake or real
#         result = detect_deepfake_audio(audio_file_path)
        
#         # Logic to handle when the call is picked up
#         return jsonify({"success": True, "message": "Call picked", "audio_result": result})
#     else:
#         return jsonify({"success": False, "message": "No audio files found"})

# # Route for hanging up the call
# @app.route("/hang", methods=["POST"])
# def hang():
#     global player
#     if player:
#         player.pause()
#     # Logic to handle when the call is hung up
#     return jsonify({"success": True, "message": "Call hung up"})

# if __name__ == "__main__":
#     load_deepfake_model()
#     app.run(debug=True)
