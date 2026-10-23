import numpy as np
import matplotlib.pyplot as plt

axa1 = np.linspace(-np.pi / 2, np.pi / 2, 10000)

pade = lambda x: (x - (7 * (x ** 3) / 60)) / (1 + (x ** 2) / 20)

eroarea_taylor = np.abs(axa1 - np.sin(axa1))
eroarea_pade = np.abs(np.sin(axa1) - pade(axa1))

fig, ax = plt.subplots(4)

ax[0].set_title("Graficele impreuna")
ax[0].plot(axa1, axa1)
ax[0].plot(axa1, np.sin(axa1))

ax[1].set_title("Error Taylor")
ax[1].plot(axa1, eroarea_taylor)

ax[2].set_title("Graficele impreuna (Pade)")
ax[2].plot(axa1, axa1)
ax[2].plot(axa1, pade(axa1))

ax[3].set_title("Errors Pade")
ax[3].plot(axa1, eroarea_pade)

plt.savefig("ex8/ex8.pdf")
plt.show()

fig, ax = plt.subplots(4)

ax[0].set_title("Graficele impreuna")
ax[0].semilogy(axa1, axa1)
ax[0].semilogy(axa1, np.sin(axa1))

ax[1].set_title("Errors Taylor")
ax[1].semilogy(axa1, eroarea_taylor)

ax[2].set_title("Graficele impreuna (Pade)")
ax[2].semilogy(axa1, np.sin(axa1))
ax[2].semilogy(axa1, pade(axa1))

ax[3].set_title("Errors (Pade)")
ax[3].semilogy(axa1, eroarea_pade)


plt.savefig("ex8/ex8_log.pdf")
plt.show()

plt.figure()
plt.yscale('log')
plt.plot(axa1, eroarea_taylor)
plt.plot(axa1, eroarea_pade)
plt.savefig("ex8/erori_impreuna.pdf")
plt.show()