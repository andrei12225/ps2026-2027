import numpy as np
import matplotlib.pyplot as plt

A = 1
fs = 1500

semnal1 = lambda x: A * np.sin(2 * np.pi * fs / 2 * x)
semnal2 = lambda x: A * np.sin(2 * np.pi * fs / 4 * x)
semnal3 = lambda x: A * np.sin(2 * np.pi * 0 * x)

axa1 = np.linspace(0, 1, fs)

fig, ax = plt.subplots(3)

ax[0].set_xlim([0, 0.3])
ax[0].plot(axa1, semnal1(axa1))
ax[1].set_xlim([0, 0.3])
ax[1].plot(axa1, semnal2(axa1))
ax[2].set_xlim([0, 0.3])
ax[2].plot(axa1, semnal3(axa1))

plt.savefig("ex6/ex6.pdf")
plt.show()