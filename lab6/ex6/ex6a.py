import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab6/Train.csv', delimiter=',', skip_header=1, usecols=2, dtype=float)
start = 1 * 24
stop =  4 * 24
x = x[start:stop]

axa = np.arange(start, stop)

plt.plot(axa, x)
plt.savefig("lab6/ex6/ex6a.pdf")
plt.show()