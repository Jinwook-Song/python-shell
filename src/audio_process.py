import librosa
import pandas as pd

AUDIO_PATH = "./assets/audio_sample.wav"
y, sr = librosa.load(AUDIO_PATH, sr=None)
y_Series = pd.Series(y)

librosa.feature.chroma_stft

print(f"duration: {len(y)/sr}")
print(f"sampling rate: {sr}")
print(f"Series: {y_Series}")
