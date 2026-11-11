import numpy as np
import matplotlib.pyplot as plt
import time

def fft(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    if N == 1:
        return x
    E = fft(x[::2])
    O = fft(x[1::2])
    w = np.exp(-2 * np.pi * 1j * np.arange(N // 2) / N)

    return np.concatenate([E + w * O, E - w * O])

def dft(signal, N):
    X = np.zeros((N), dtype=complex)
    for w in range(0, N):
        s = 0
        for n in range(0, N):
            s += signal[n] * np.exp(-2 * np.pi * 1j * n * w / N)
        X[w] = s
    return X

a1, f1 = 1, 6
a2, f2 = 2, 10
a3, f3 = 0.5, 15

Ns = [128, 256, 512, 1024, 2048, 4096, 8192]

times_numpy = []
times_dft = []
times_fft = []

for N in Ns:
    nts = np.linspace(0, 1, N)
    signal = a1 * np.cos(2 * np.pi * f1 * nts) + a2 * np.cos(2 * np.pi * f2 * nts) + a3 * np.cos(2 * np.pi * f3 * nts)

    time_numpy_i = time.perf_counter()
    np.fft.fft(signal, N)
    time_numpy_f = time.perf_counter()
    time_numpy = (time_numpy_f - time_numpy_i)

    time_dft_i = time.perf_counter()
    dft(signal, N)
    time_dft_f = time.perf_counter()
    time_dft = time_dft_f - time_dft_i

    time_fft_i = time.perf_counter()
    fft(signal)
    time_fft_f = time.perf_counter()
    time_fft = time_fft_f - time_fft_i

    times_numpy.append(time_numpy)
    times_dft.append(time_dft)
    times_fft.append(time_fft)

plt.semilogy(Ns, times_numpy, label="Numpy FFT")
plt.semilogy(Ns, times_dft, label="DFT")
plt.semilogy(Ns, times_fft, label="FFT")
plt.xlabel("N")
plt.ylabel("Timp (s)")
plt.xticks(Ns)
plt.legend()
plt.savefig("lab4/ex1/ex1.pdf")
plt.show()