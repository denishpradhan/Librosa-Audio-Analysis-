import librosa 

y,sr = librosa.load('trying.wav',sr=None) # sr=None to preserve original sample rate

print("Sample rate:",sr,"Samples per second")
print("Number of Samples:",len(y),"total samples in the audio")
print("Duration of the audio:",len(y)/sr,"seconds")