import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab6/Train.csv', delimiter=',', skip_header=1, usecols=2, dtype=float)
start = 1 * 24
stop =  4 * 24
x = x[start:stop]

ws = [5, 9, 13, 17]

fig, ax = plt.subplots(len(ws))

axa_x = np.arange(start, stop)

for i, w in enumerate(ws):
    x_conv = np.convolve(x, np.ones(w), 'valid') / w
    axa = np.arange(len(x_conv)) + start + (w - 1) // 2
    ax[i].grid()
    ax[i].plot(axa_x, x, alpha=0.4, label='original')
    ax[i].plot(axa, x_conv, label=f'w = {w}')
    ax[i].legend()

plt.savefig("lab6/ex6/ex6b.pdf")
plt.show()