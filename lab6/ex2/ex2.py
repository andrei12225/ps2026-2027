import numpy as np
import matplotlib.pyplot as plt

N = 100


def itereaza(x, nr_iter=3):
    rezultate = [x]
    for _ in range(nr_iter):
        x = np.convolve(x, x)
        rezultate.append(x)
    return rezultate


def afiseaza(rezultate, titlu):
    fig, ax = plt.subplots(len(rezultate))
    fig.suptitle(titlu)
    for i, r in enumerate(rezultate):
        ax[i].plot(r / np.max(np.abs(r)))  # normalizat, altfel valorile explodeaza
        ax[i].grid()
    fig.tight_layout()


x_aleator = np.random.rand(N)
afiseaza(itereaza(x_aleator), 'Semnal aleator')

x_bloc = np.zeros(N)
x_bloc[45:55] = 1
afiseaza(itereaza(x_bloc), 'Bloc rectangular')

plt.savefig('lab6/ex2/ex2.pdf')
plt.show()
