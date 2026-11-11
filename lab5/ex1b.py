import numpy as np
import datetime as dt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=1, dtype=str)

x = [dt.datetime.strptime(z, '%d-%m-%Y %H:%S') for z in x]

print("Intervalul de timp este:")
print(min(x), max(x))
