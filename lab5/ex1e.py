import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600 

# Da, semnalul are o componenta continua (am scos-o scazand media)

X = np.fft.fft(x - np.mean(x))
X = abs(X) / N
X = X[:(N//2)]

f = Fs * np.arange(N//2) / N

plt.plot(f, X)
plt.savefig("./lab5/ex1e.pdf")
plt.show()