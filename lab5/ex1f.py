import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600 

X = np.fft.fft(x)
X = abs(X) / N
X = X[:(N//2)]

Y = sorted(list(enumerate(X)), key=lambda z: z[1], reverse=True)
f = Fs * np.arange(N//2) / N

print("Cele mai mari 4 valori ale modulului:")
print([z[1] for z in Y[:4]])
print("Frecvente in Hz corespunzatoare:")
print([f[z[0]] for z in Y[:4]])
print("Frecvente in zile? corespunzatoare:")
print([f[z[0]]*86400 for z in Y[:4]])