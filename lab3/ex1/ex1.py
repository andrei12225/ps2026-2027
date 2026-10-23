import numpy as np
import matplotlib.pyplot as plt
import math

a1, f1 = 1, 5
a2, f2 = 2, 20
a3, f3 = 0.5, 75

nts = np.linspace(0, 1, 1000)
signal = lambda nts: a1 * np.cos(2 * np.pi * f1 * nts) + a2 * np.cos(2 * np.pi * f2 * nts) + a3 * np.cos(2 * np.pi * f3 * nts)

N = 8

fix, axs = plt.subplots(N)

matrix = np.zeros((8, 8), dtype=complex)

for m in range(0, N):
    for k in range(0, N):
        exp_complexa = np.exp(-2 * np.pi * 1j * m / N * k)
        matrix[m][k] = exp_complexa

    axa_x = np.arange(N)

    axs[m].plot(axa_x, matrix[m].real, marker='o')
    axs[m].plot(axa_x, matrix[m].imag, marker='o')

plt.savefig("ex1/ex1.pdf")

plt.show()

# Trebuie sa scalam ca matricea sa fie ortonormala
matrix = 1 / np.sqrt(N) * matrix

print(np.allclose(np.matrix(matrix).H * matrix, np.identity(8)))   