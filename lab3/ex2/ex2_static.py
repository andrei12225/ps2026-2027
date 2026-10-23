import numpy as np
import matplotlib.pyplot as plt

a, f = 1, 17

nts = np.linspace(0, 1, 5000)
signal = lambda nts: a * np.sin(2 * np.pi * f * nts)

y = lambda w, nts: signal(nts) * np.exp(-2 * np.pi * 1j * nts * w)
y_1 = y(1, nts)

fig, (ax1, ax2) = plt.subplots(1, 2)

dist = np.sqrt(nts ** 2 + signal(nts) ** 2)
dist_y = lambda w: np.sqrt(y(w, nts).real ** 2 + y(w, nts).imag ** 2)

ax1.scatter(nts, signal(nts), c=dist, cmap='Reds_r', marker=',')
ax1.stem(nts[620], signal(nts[620]), markerfmt='blue', linefmt='blue')

ax2.scatter(y_1.real, y_1.imag, c=dist_y(1), cmap='Reds_r', marker=',')
ax2.plot([0, y_1[620].real], [0, y_1[620].imag], color='blue', marker='o')

ax1.grid()
ax2.grid()

plt.savefig("ex2/ex2_fig1_static.pdf")
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 2)

ax1[0].scatter(y(1, nts).real, y(1, nts).imag, c=dist_y(1), cmap='Reds_r', marker=',')
ax1[1].scatter(y(2, nts).real, y(2, nts).imag, c=dist_y(2), cmap='Reds_r', marker=',')
ax2[0].scatter(y(5, nts).real, y(5, nts).imag, c=dist_y(5), cmap='Reds_r', marker=',')
ax2[1].scatter(y(17, nts).real, y(17, nts).imag, c=dist_y(17), cmap='Reds_r', marker=',')

ax1[0].grid()
ax1[1].grid()
ax2[0].grid()
ax2[1].grid()

plt.savefig("ex2/ex2_fig2_static.pdf")
plt.show()