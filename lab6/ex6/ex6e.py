import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

x = np.genfromtxt('./lab6/Train.csv', delimiter=',', skip_header=1, usecols=2, dtype=float)
start = 1 * 24
stop = 4 * 24
x = x[start:stop]
axa = np.arange(start, stop)

ordin = 5
Wn = 1 / 3  # de la c)
rp = 5      # de la d)

b_butter, a_butter = scipy.signal.butter(ordin, Wn, btype='low')
b_cheby, a_cheby = scipy.signal.cheby1(ordin, rp, Wn, btype='low')

x_butter = scipy.signal.filtfilt(b_butter, a_butter, x)
x_cheby = scipy.signal.filtfilt(b_cheby, a_cheby, x)

plt.plot(axa, x, alpha=0.4, label='date brute')
plt.plot(axa, x_butter, label='Butterworth')
plt.plot(axa, x_cheby, label=f'Chebyshev (rp = {rp} dB)')
plt.xlabel('Ora')
plt.ylabel('Numar de vehicule')
plt.grid()
plt.legend()
plt.savefig("lab6/ex6/ex6e.pdf")
plt.show()
