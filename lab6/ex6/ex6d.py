import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

ordin = 5
Wn = 1 / 3        # de la c)
rps = [1, 5, 10] 

b_butter, a_butter = scipy.signal.butter(ordin, Wn, btype='low')

w, h = scipy.signal.freqz(b_butter, a_butter)
plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), label='Butterworth')

for rp in rps:
    b_cheby, a_cheby = scipy.signal.cheby1(ordin, rp, Wn, btype='low')
    w, h = scipy.signal.freqz(b_cheby, a_cheby)
    plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), label=f'Chebyshev rp = {rp} dB')

plt.axvline(Wn, color='k', linestyle='--', label=f'Wn = {Wn:.2f}')
plt.xlabel('Frecventa normalizata')
plt.ylabel('Amplitudine (dB)')
plt.ylim(-80, 5)
plt.grid()
plt.legend()
plt.savefig("lab6/ex6/ex6d.pdf")
plt.show()
