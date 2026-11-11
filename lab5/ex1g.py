import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

x = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=2)
xd = np.genfromtxt('./lab5/Train.csv', delimiter=',', skip_header=1, usecols=1, dtype=str)
xd = [dt.datetime.strptime(z, '%d-%m-%Y %H:%M') for z in xd]

start = 1000
idx = next(i for i in range(start + 1, len(xd))
           if xd[i].weekday() == 0 and xd[i].hour == 0)
print(idx, xd[idx])   

L = 24 * 30           
x_luna = x[idx:idx + L]
t_luna = xd[idx:idx + L]

plt.figure(figsize=(12, 4))
plt.plot(t_luna, x_luna)
plt.savefig("./lab5/ex1g.pdf")
plt.show()