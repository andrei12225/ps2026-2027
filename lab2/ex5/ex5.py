import numpy as np
import matplotlib.pyplot as plt
import sounddevice

A = 1
fs = 44100

semnal1 = lambda x: A * np.sin(2 * np.pi * 441 * x)
semnal2 = lambda x: A * np.sin(2 * np.pi * 560 * x)

axa1 = np.linspace(0, 2, 2 * fs)

vector = np.concatenate([semnal1(axa1), semnal2(axa1)])

sounddevice.play(vector, samplerate=fs)
sounddevice.wait()
