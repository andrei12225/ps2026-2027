from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

fs, x = wavfile.read("./lab4/ex6/vocale.wav")   # fs = frecvența de eșantionare, x = vectorul

N = len(x)

L = N // 100
P = L // 2

grupuri = []

for i in range(0, N - L + 1, P):
    grupuri.append(x[i : i + L])

L = len(grupuri[0])
spectograma = np.zeros((L, len(grupuri)), dtype=float)

for i, grup in enumerate(grupuri):
    fft = np.abs(np.fft.fft(grup))
    spectograma[:, i] = fft

spec_db = 20 * np.log10(spectograma + 1e-10)

durata = len(x) / fs
plt.imshow(spec_db, aspect='auto', origin='lower',
           extent=[0, durata, 0, fs / 2 / 1000], cmap='magma')
plt.xlabel('Timp (s)')
plt.ylabel('Frecventa')
plt.colorbar(label='dB')
plt.savefig("./lab4/ex6/ex6.pdf")
plt.show()
