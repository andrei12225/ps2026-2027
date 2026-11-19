import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab6/Train.csv', delimiter=',', skip_header=1, usecols=2, dtype=float)
start = 1 * 24
stop =  4 * 24
x = x[start:stop]

N = len(x)
Fs = 1 / 3600  # un esantion pe ora

X = np.fft.fft(x - np.mean(x))  # scadem media, altfel componenta continua (f = 0) domina graficul
X = abs(X) / N                  
X = X[:N // 2]                  

f = Fs * np.arange(N // 2) / N  

# Frecventa de taiere: pastram variatiile cu perioada >= 6 ore (ciclul zilnic)
# fluctuatiile mai rapide (de la o ora la alta) le
# consideram zgomot.
T_taiere = 6 * 3600                 
f_c = 1 / T_taiere                 
f_nyquist = Fs / 2                
Wn = f_c / f_nyquist                

print(f'Frecventa de taiere: {f_c:.3e} Hz')
print(f'Frecventa normalizata: {Wn:.3f}')

plt.plot(f, X)
plt.axvline(f_c, color='r', linestyle='--', label=f'f_c = {f_c:.2e} Hz (Wn = {Wn:.2f})')
plt.legend()
plt.xlabel('Frecventa (Hz)')
plt.ylabel('|X(f)|')
plt.grid()
plt.savefig("lab6/ex6/ex6c.pdf")
plt.show()