import numpy as np

n = 20
d_init = 3
x = np.random.randint(-10, 11, n)
y = np.roll(x, d_init)

d = np.real(np.fft.ifft(np.conj(np.fft.fft(x)) * np.fft.fft(y)))
d = np.argmax(d)

print(f'd initial: {d_init}')
print(f'd dupa prima formula: {d}')

d = np.real(np.fft.ifft(np.fft.fft(y) / np.fft.fft(x)))
d = np.argmax(d)

print(f'd dupa a doua formula: {d}')