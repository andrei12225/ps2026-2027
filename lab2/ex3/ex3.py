import numpy as np
import matplotlib as plt
import sounddevice
import scipy.io

A = 1

semnal = lambda x, f: A * np.sin(2 * np.pi * f * x)
sawtooth = lambda x, f: np.mod(f * x, 1)
square = lambda x, f: np.sign(semnal(x, f))

fs = 44100
axa1 = np.arange(0, 3, 1 / fs)

semnal_a = semnal(axa1, 400)
semnal_b = semnal(axa1, 800)
semnal_c = sawtooth(axa1, 240)
semnal_d = square(axa1, 300)

sounddevice.play(semnal_a, samplerate=fs)
sounddevice.wait()

sounddevice.play(semnal_b, samplerate=fs)
sounddevice.wait()

sounddevice.play(semnal_c, samplerate=fs)
sounddevice.wait()

sounddevice.play(semnal_d, samplerate=fs)
sounddevice.wait()

scipy.io.wavfile.write("ex3/semnal_a.wav", fs, semnal_a)