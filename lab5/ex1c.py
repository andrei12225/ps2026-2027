import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=2)
N = len(x)
Fs = 1 / 3600 

print(Fs / 2)