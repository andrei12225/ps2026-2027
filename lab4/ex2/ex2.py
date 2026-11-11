import numpy as np
import matplotlib.pyplot as plt

f1 = 5
signal = lambda t: np.sin(2 * np.pi * f1 * t)
f2 = 13
signal2 = lambda t: np.sin(2 * np.pi * f2 * t)
f3 = 18
signal3 = lambda t: np.sin(2 * np.pi * f3 * t)

fs = 8 # Hz

esantioane = np.linspace(0, 1, fs)

fig, ax = plt.subplots(4)

ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[0].plot(esantioane, signal(esantioane))
ax[1].plot(esantioane, signal(esantioane))
ax[1].stem(esantioane[:-1], signal(esantioane[:-1]))
ax[2].plot(esantioane, signal2(esantioane))
ax[2].stem(esantioane[:-1], signal2(esantioane[:-1]))
ax[3].plot(esantioane, signal3(esantioane))
ax[3].stem(esantioane[:-1], signal3(esantioane[:-1]))

plt.savefig("./lab4/ex2/ex2.pdf")
plt.show()
