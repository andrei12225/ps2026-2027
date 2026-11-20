import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600

# Alegerea frecventei de taiere:
# Din ex1f, componentele dominante sunt trendul (frecvente foarte mici),
# ciclul saptamanal si ciclul zilnic (1 / 86400 Hz).
# Pastram tot ce are perioada >= 12 ore (fc = 1 / (12 * 3600) Hz)
# Ce e peste fc este zgomot
fc = 1 / (12 * 3600)

X = np.fft.fft(x)
f = np.fft.fftfreq(N, d=1/Fs)  

X_filtrat = X.copy()
X_filtrat[np.abs(f) > fc] = 0 

x_filtrat = np.real(np.fft.ifft(X_filtrat))


start, L = 1000, 24 * 30
plt.figure(figsize=(12, 4))
plt.plot(x[start:start + L], label='original')
plt.plot(x_filtrat[start:start + L], label='filtrat (perioade >= 12h)')
plt.xlabel('ore')
plt.legend()
plt.savefig("./lab5/ex1i.pdf")
plt.show()
