import librosa
import matplotlib.pyplot as plt
import os

# Change to the script's directory
os.chdir(os.path.dirname(__file__))

# Loading an audio file
print("Loading audio file...")
waveform, sample_rate = librosa.load('trying.wav')
print(f"Loaded waveform with shape {waveform.shape}, sample rate {sample_rate}")

# create a window
plt.figure(figsize=(10, 4))

# plot the waveformRHS
librosa.display.waveshow(waveform, sr=sample_rate, color='blue')

# Add title and labels
plt.title('Waveform of the Audio')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# adjust the layout
plt.tight_layout()

# save the plot instead of showing
plt.savefig('waveform.png')
print("Plot saved as waveform.png")
# plt.show()
