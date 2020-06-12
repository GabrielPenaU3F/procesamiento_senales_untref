import numpy as np
import scipy.signal as sig

from ejemplos.practica_2.funciones import generar_senoide
from matplotlib import pyplot as plt

fs = 44100
t1, x = generar_senoide(0, 3, 2, 50, 0, fs)
t2, y = generar_senoide(0, 3, 2, 400, 0, fs)
t3, w = generar_senoide(0, 3, 2, 20000, 0, fs)
t4, u = generar_senoide(0, 6, 2, 50, 0, fs)
t5, v = generar_senoide(0, 6, 2, 400, 0, fs)
t0, silencio = generar_senoide(0, 3, 0, 400, 0, fs)

z1 = np.concatenate((x, y), axis=None)
z2 = np.concatenate((x, w, y), axis=None)
z3 = np.concatenate((silencio, w), axis=None) + u + v

f, t, spect = sig.spectrogram(z3, fs)
plt.pcolormesh(t, f, spect)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
