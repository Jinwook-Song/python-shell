import librosa

audio_path = "./assets/audio_sample.wav"
y, sr = librosa.load(audio_path, sr=None)

print(f"duration: {len(y)/sr}")
print(f"sampling rate: {sr}")
