import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600 

X = np.fft.fft(x)
X = abs(X) / N
X = X[:(N//2)]

f = Fs * np.arange(N//2) / N

xmax = max(list(enumerate(X)), key=lambda z: z[1])

print("Frecventa maxima:")
print(f[xmax[0]])