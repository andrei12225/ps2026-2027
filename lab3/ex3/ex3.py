import numpy as np
import matplotlib.pyplot as plt

a1, f1 = 1, 6
a2, f2 = 2, 10
a3, f3 = 0.5, 15

N = 1000

nts = np.linspace(0, 1, N)
signal = a1 * np.cos(2 * np.pi * f1 * nts) + a2 * np.cos(2 * np.pi * f2 * nts) + a3 * np.cos(2 * np.pi * f3 * nts)

fig, ax = plt.subplots(2)

ax[0].plot(nts, signal)

X = np.zeros((N), dtype=complex)

for w in range(0, N):
    s = 0
    for n in range(0, N):
        s += signal[n] * np.exp(-2 * np.pi * 1j * n * w / N)
    X[w] = s

frecv = np.arange(0, N)
ax[1].stem(frecv, np.abs(X))

plt.savefig("ex3/ex3.pdf")
plt.show()