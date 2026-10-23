import numpy as np
import matplotlib.pyplot as plt

a, f = 1, 17

nts = np.linspace(0, 1, 1000)
signal = lambda nts: a * np.sin(2 * np.pi * f * nts)

y = lambda w, nts: signal(nts) * np.exp(-2 * np.pi * 1j * nts * w)
y_1 = y(1, nts)

plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.grid()
ax2.grid()

ax1.set_ylim(-1, 1)
ax2.set_ylim(-1, 1)

line1, = ax1.plot([], [])
line2, = ax2.plot([], [])

marker1, = ax1.plot([], [], marker='o', color='red')
marker2, = ax2.plot([], [], marker='o', color='red')

vect = signal(nts)

for i in range(1, len(nts) + 1):
    curr_x = nts[:i]
    curr_y = vect[:i]

    line1.set_data(curr_x, curr_y)
    ax1.set_xlim(curr_x[-1] - 0.2, curr_x[-1] + 0.1)
    marker1.set_data([curr_x[-1]], [curr_y[-1]])

    line2.set_data(y_1.real[:i], y_1.imag[:i])
    ax2.set_xlim(y_1.real[-1] - 1, y_1.imag[-1] + 1)
    marker2.set_data([y_1.real[:i][-1]], [y_1.imag[:i][-1]])

    plt.pause(0.005)

plt.ioff()
plt.show()

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 2)

ax1[0].grid()
ax1[1].grid()
ax2[0].grid()
ax2[1].grid()

ax1[0].set_ylim(-2, 2)
ax1[1].set_ylim(-2, 2)
ax2[0].set_ylim(-2, 2)
ax2[1].set_ylim(-2, 2)

line1, = ax1[0].plot([], [])
line2, = ax1[1].plot([], [])
line3, = ax2[0].plot([], [])
line4, = ax2[1].plot([], [])

marker1, = ax1[0].plot([], [], marker='o', color='red')
marker2, = ax1[1].plot([], [], marker='o', color='red')
marker3, = ax2[0].plot([], [], marker='o', color='red')
marker4, = ax2[1].plot([], [], marker='o', color='red')

for i in range(1, len(nts) + 1):
    line1.set_data(y_1.real[:i], y_1.imag[:i])
    marker1.set_data([y_1.real[:i][-1]], [y_1.imag[:i][-1]]) 
    ax1[0].set_xlim(y_1.real[-1] - 1, y_1.imag[-1] + 1)

    line2.set_data(y(2, nts).real[:i], y(2, nts).imag[:i])
    marker2.set_data([y(2, nts).real[:i][-1]], [y(2, nts).imag[:i][-1]]) 
    ax1[1].set_xlim(y(2, nts).real[-1] - 1, y(2, nts).imag[-1] + 1)

    line3.set_data(y(5, nts).real[:i], y(5, nts).imag[:i])
    marker3.set_data([y(5, nts).real[:i][-1]], [y(5, nts).imag[:i][-1]])
    ax2[0].set_xlim(y(5, nts).real[-1] - 1, y(5, nts).imag[-1] + 1)

    line4.set_data(y(17, nts).real[:i], y(17, nts).imag[:i])
    marker4.set_data([y(17, nts).real[:i][-1]], [y(17, nts).imag[:i][-1]]) 
    ax2[1].set_xlim(y(17, nts).real[-1] - 1, y(17, nts).imag[-1] + 1)

    plt.pause(0.005)

plt.ioff()
plt.show()