import numpy as np
import matplotlib.pyplot as plt

A = 1

semnal = lambda x: A * np.sin(2 * np.pi * 3 * x)
sawtooth = lambda x: np.mod(3 * x, 1)

axa1 = np.linspace(0, 1, 1500)

fig, ax = plt.subplots(3)

ax[0].plot(axa1, semnal(axa1))
ax[1].plot(axa1, sawtooth(axa1))
ax[2].plot(axa1, semnal(axa1) + sawtooth(axa1))

plt.savefig("ex4/ex4.pdf")
plt.show()