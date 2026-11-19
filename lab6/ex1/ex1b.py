import numpy as np
import matplotlib.pyplot as plt

B = 1
x = lambda t: np.sinc(B * t) ** 2
fss = [1, 1.5, 2, 4]

fig, ax = plt.subplots(len(fss))

def calc_reconstr(xn, tn, t, fs):
    Ts = 1 / fs
    s = np.zeros_like(t)
    for n in range(len(xn)):
        s += xn[n] * np.sinc((t - tn[n]) / Ts)
    return s

for i, fs in enumerate(fss):  
    axa = np.arange(-3, 3, 1 / 1000)
    esantioane = np.arange(-3, 3, 1 / fs)

    xn = x(esantioane)

    ax[i].grid()
    ax[i].plot(axa, x(axa))
    ax[i].plot(axa, calc_reconstr(xn, esantioane, axa, fs), '--')
    ax[i].stem(esantioane, xn, basefmt='none')

plt.savefig("lab6/ex1/ex1.pdf")
plt.show()