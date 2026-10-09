import numpy as np
import matplotlib.pyplot as plt

# t = timpul
x = lambda t: np.cos(520 * np.pi * t + np.pi / 3)
y = lambda t: np.cos(280 * np.pi * t - np.pi / 3)
z = lambda t: np.cos(120 * np.pi * t + np.pi / 3)

axa_timp = np.arange(0, 0.03, 0.0005)

fig, axs = plt.subplots(3)

axs[0].plot(axa_timp, x(axa_timp))
axs[1].plot(axa_timp, y(axa_timp))
axs[2].plot(axa_timp, z(axa_timp))

plt.savefig("ex1/ex1b.pdf")

plt.show()

fig, axs = plt.subplots(3)

f0 = 200
axa_timp_f0 = np.arange(0, 0.03, 1 / f0)

axs[0].plot(axa_timp, x(axa_timp))
axs[0].stem(axa_timp_f0, x(axa_timp_f0))
axs[1].plot(axa_timp, y(axa_timp))
axs[1].stem(axa_timp_f0, y(axa_timp_f0))
axs[2].plot(axa_timp, z(axa_timp))
axs[2].stem(axa_timp_f0, z(axa_timp_f0))

plt.savefig("ex1/ex1c.pdf")

plt.show()