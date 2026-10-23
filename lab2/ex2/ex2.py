import numpy as np
import matplotlib.pyplot as plt

faze = [1, 4, 8, 16]
semnal_sinus = lambda t, faza: 1 * np.sin(2 * np.pi * 5 * t + faza)

esantioane = np.linspace(0, 1, 5000)

for faza in faze:
    plt.plot(esantioane, semnal_sinus(esantioane, faza))

plt.savefig("ex2/ex2a.pdf")
plt.show()

faza = 4
semnal_sinus = lambda t: 1 * np.sin(2 * np.pi * 5 * t + faza)

distributie_gaussiana = np.random.normal(size=5000)
toate_snr = [0.1, 1, 10, 100]

fig, ax = plt.subplots(4)

for i, snr in enumerate(toate_snr):
    semnal_sinus_v = semnal_sinus(esantioane)
    gamma = np.linalg.norm(semnal_sinus_v) / (np.sqrt(snr) * np.linalg.norm(distributie_gaussiana))
    semnal_nou = semnal_sinus_v + gamma * distributie_gaussiana

    ax[i].plot(esantioane, semnal_nou)

plt.savefig("ex2/ex2b.pdf")
plt.show()