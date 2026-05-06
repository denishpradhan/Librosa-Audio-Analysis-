import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load audio file
file_path = "audio.wav"  # change this
y, sr = librosa.load('trying.wav')

print("Sample Rate:", sr)
print("Audio Data Shape:", y.shape)

# Plot waveform
plt.figure(figsize=(10, 4))
plt.plot(y)
plt.title("Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()

# Extract features
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
print("Tempo (BPM):", tempo)

# Spectrogram
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.title("Spectrogram")
plt.colorbar()
plt.show()