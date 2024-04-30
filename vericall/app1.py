import joblib
import librosa
import numpy as np

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

if __name__ == "__main__":
    model_path = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\aiaudio\random_forest_model.joblib"
    audio_file = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\data\fake\LJ001-0001_gen.wav"

    model = load_model(model_path)
    result = detect_deepfake_audio(audio_file, model)
    print("Prediction:", result)


# import joblib
# import librosa

# def load_model(model_path):
#     return joblib.load(model_path)

# def extract_features(audio_file, n_mfcc=40, hop_length=512, n_fft=2048):
#     y, sr = librosa.load(audio_file)
#     mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, hop_length=hop_length, n_fft=n_fft)
#     return mfccs.T

# def detect_deepfake_audio(audio_file, model):
#     features = extract_features(audio_file)
#     prediction = model.predict(features)
#     if prediction[0] == 0:
#         return "Real"
#     else:
#         return "Fake"

# if __name__ == "__main__":
#     model_path = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\aiaudio\random_forest_model.joblib"
#     audio_file = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\aiaudio\test\fake.wav"
#     model = load_model(model_path)
#     result = detect_deepfake_audio(audio_file, model)
#     print("Prediction:", result)

