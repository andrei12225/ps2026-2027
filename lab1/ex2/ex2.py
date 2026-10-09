import numpy as np
import matplotlib.pyplot as plt

A = 1
s1 = lambda x, f: A * np.sin(2 * np.pi * f * x)
sawtooth = lambda x, f: np.mod(f * x, 1)
square = lambda x, f: np.sign(s1(x, f))
axa1 = np.linspace(0, 0.2, 1600)
axa2 = np.linspace(0, 3, 2000)

plt.figure()
plt.plot(axa1, s1(axa1, 400))
plt.savefig("ex2/ex2a.pdf")
plt.show()

plt.figure()
plt.xlim(right=0.5)
plt.plot(axa2, s1(axa2, 800))
plt.savefig("ex2/ex2b.pdf")
plt.show()

plt.figure()
plt.plot(axa1, sawtooth(axa1, 240))
plt.savefig("ex2/ex2c.pdf")
plt.show()

plt.figure()
plt.plot(axa1, square(axa1, 300))
plt.savefig("ex2/ex2d.pdf")
plt.show()

plt.figure()
s2 = np.random.rand(128, 128)
plt.imshow(s2)
plt.savefig("ex2/ex2e.pdf")
plt.show()

plt.figure()
s3 = np.zeros((128, 128))
s3[0:128, 0:10] = 1
s3[0:50, 5:50] = 1
s3[0:10, 80:128] = 1
s3[10:50, 80:90] = 1
s3[50:60, 80:128] = 1
s3[60:120, 120:128] = 1
s3[120:128, 80:128] = 1
plt.imshow(s3)
plt.savefig("ex2/ex2f.pdf")
plt.show()