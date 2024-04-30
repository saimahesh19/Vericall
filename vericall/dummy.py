import os
import random
import pygame

def play_random_audio(folder_path):
    # Get list of folders (real and fake)
    folder_list = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
    
    # Choose a random folder (real or fake)
    chosen_folder = random.choice(folder_list)
    
    # Display whether the chosen folder is real or fake
    if chosen_folder == 'real':
        print("Chosen folder: Real")
    else:
        print("Chosen folder: Fake")
    
    # Get list of audio files in the chosen folder
    audio_files = [file for file in os.listdir(os.path.join(folder_path, chosen_folder)) if file.endswith('.wav')]
    
    if not audio_files:
        print("No audio files found in the chosen folder.")
        return
    
    # Choose a random audio file from the chosen folder
    chosen_audio = random.choice(audio_files)
    
    # Load and play the chosen audio file
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(folder_path, chosen_folder, chosen_audio))
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Display message based on the chosen folder
    if chosen_folder == 'fake':
        print("Audio is deepfaked.")
    else:
        print("Audio is original.")

if __name__ == "__main__":
    folder_path = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\audios"
    play_random_audio(folder_path)
