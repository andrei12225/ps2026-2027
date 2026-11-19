import numpy as np
import matplotlib.pyplot as plt


def fereastra_dreptunghiulara(N):
    return np.ones(N)


def fereastra_hanning(N):
    n = np.arange(N)
    return 0.5 * (1 - np.cos(2 * np.pi * n / (N - 1)))


f = 100
A = 1
phi = 0
Nw = 200
fs = 8000 

N = 600 
n = np.arange(N)
t = n / fs
x = A * np.sin(2 * np.pi * f * t + phi)

start = (N - Nw) // 2
w_drept = np.zeros(N)
w_drept[start:start + Nw] = fereastra_dreptunghiulara(Nw)
w_hann = np.zeros(N)
w_hann[start:start + Nw] = fereastra_hanning(Nw)

fig, ax = plt.subplots(3)

ax[0].plot(t, x)
ax[0].set_title('Sinusoida originala')

ax[1].plot(t, x * w_drept)
ax[1].plot(t, w_drept, '--')
ax[1].set_title('Fereastra dreptunghiulara')

ax[2].plot(t, x * w_hann)
ax[2].plot(t, w_hann, '--')
ax[2].set_title('Fereastra Hanning')

for a in ax:
    a.grid()
fig.tight_layout()

plt.savefig("lab6/ex5/ex5.pdf")
plt.show()
