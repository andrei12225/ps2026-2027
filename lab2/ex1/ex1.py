import numpy as np
import matplotlib.pyplot as plt

semnal_sinus = lambda t: 2 * np.sin(2 * np.pi * 5 * t + 3)
semnal_cosinus = lambda t: 2 * np.cos(2 * np.pi * 5 * t + 3 - np.pi / 2)

esantioane = np.linspace(0, 1, 5000)

fig, ax = plt.subplots(2)

ax[0].plot(esantioane, semnal_sinus(esantioane))
ax[1].plot(esantioane, semnal_cosinus(esantioane))

plt.savefig("ex1/ex1.pdf")
plt.show()