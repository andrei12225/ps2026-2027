import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

x = np.genfromtxt('./lab6/Train.csv', delimiter=',', skip_header=1, usecols=2, dtype=float)
start = 1 * 24
stop = 4 * 24
x = x[start:stop]
axa = np.arange(start, stop)

Wn = 1 / 3  # de la c)

ordine = [2, 5, 9]
rps = [0.5, 1, 5, 10]
rp_fix = 1     # rp folosit cand variem ordinul la Chebyshev
ordin_fix = 5  # ordinul folosit cand variem rp

fig, ax = plt.subplots(3, 2, figsize=(12, 10))

# coloana 0: semnalele filtrate, coloana 1: raspunsurile in frecventa
def deseneaza(rand, b, a, label):
    ax[rand, 0].plot(axa, scipy.signal.filtfilt(b, a, x), label=label)
    w, h = scipy.signal.freqz(b, a)
    ax[rand, 1].plot(w / np.pi, 20 * np.log10(np.abs(h) + 1e-12), label=label)

# 1. Butterworth, ordine diferite
for o in ordine:
    b, a = scipy.signal.butter(o, Wn, btype='low')
    deseneaza(0, b, a, f'Butterworth ordin {o}')

# 2. Chebyshev, ordine diferite (rp fix)
for o in ordine:
    b, a = scipy.signal.cheby1(o, rp_fix, Wn, btype='low')
    deseneaza(1, b, a, f'Chebyshev ordin {o}, rp = {rp_fix}')

# 3. Chebyshev, rp diferit (ordin fix)
for rp in rps:
    b, a = scipy.signal.cheby1(ordin_fix, rp, Wn, btype='low')
    deseneaza(2, b, a, f'Chebyshev ordin {ordin_fix}, rp = {rp}')

for r in range(3):
    ax[r, 0].plot(axa, x, color='gray', alpha=0.3, label='date brute')
    ax[r, 0].set_xlabel('Ora')
    ax[r, 1].axvline(Wn, color='k', linestyle='--')
    ax[r, 1].set_ylim(-80, 5)
    ax[r, 1].set_xlabel('Frecventa normalizata')
    ax[r, 1].set_ylabel('dB')
    for c in range(2):
        ax[r, c].grid()
        ax[r, c].legend(fontsize=7)

fig.tight_layout()
plt.savefig("lab6/ex6/ex6f.pdf")
plt.show()

# Valori alese: Butterworth ordin 5, Wn = 1/3 
# un ordin mai mare doar adauga complexitate