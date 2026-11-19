import numpy as np

N = 10 

p = np.random.randint(-10, 11, N + 1)
q = np.random.randint(-10, 11, N + 1)


def produs_direct(p, q):
    r = np.zeros(len(p) + len(q) - 1, dtype=int)
    for i in range(len(p)):
        for j in range(len(q)):
            r[i + j] += p[i] * q[j]
    return r


def produs_fft(p, q):
    L = len(p) + len(q) - 1         
    P = np.fft.fft(p, L)         
    Q = np.fft.fft(q, L)
    r = np.fft.ifft(P * Q)
    return np.round(np.real(r)).astype(int) 


r_direct = produs_direct(p, q)
r_fft = produs_fft(p, q)

print('p =', p)
print('q =', q)
print('r direct     =', r_direct)
print('r fft        =', r_fft)
print('np.convolve  =', np.convolve(p, q))
print('egale:', np.array_equal(r_direct, r_fft))
