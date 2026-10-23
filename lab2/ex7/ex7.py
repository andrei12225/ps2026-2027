import numpy as np
import matplotlib.pyplot as plt

A = 1
fs = 100

semnal1 = lambda x: A * np.sin(2 * np.pi * 5 * x)

axa1 = np.linspace(0, 1, fs)

fig, ax = plt.subplots(3)

ax[0].plot(axa1, semnal1(axa1))
ax[0].stem(axa1, semnal1(axa1))
ax[0].set_title('Normal')
ax[0].set_xlim([0, 0.3])
ax[1].plot(axa1[::4], semnal1(axa1)[::4])
ax[1].stem(axa1[::4], semnal1(axa1)[::4])
ax[1].set_xlim([0, 0.3])
ax[1].set_title('Decimat 1/4')
ax[2].plot(axa1[1::4], semnal1(axa1)[1::4])
ax[2].stem(axa1[1::4], semnal1(axa1)[1::4])
ax[2].set_xlim([0, 0.3])
ax[2].set_title('Decimat 1/4 pornind de la 2')

plt.savefig("ex7/ex7.pdf")
plt.show()