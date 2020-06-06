import numpy as np
from matplotlib import pyplot as plt

from ejemplos.practica_2.funciones import generar_senoide
from ejemplos.practica_5.funciones import calcular_transformada

duracion = 2
fs = 1000
t, x_t = generar_senoide(0, duracion, 2, 250, 0, fs)

X_w = calcular_transformada(x_t)

re_X = np.real(X_w)
im_X = np.imag(X_w)  # El coseno es real puro, asi que esto es casi nulo. Lo descarto

'''
w = np.linspace(0, 2*np.pi*fs, duracion*fs, endpoint=None)

fig, axes = plt.subplots(1, 3)
axes[0].plot(t, x_t)
axes[1].plot(w, re_X)
axes[1].set_ylim(bottom=-2000, top=2000)
axes[2].plot(w, im_X)
axes[2].set_ylim(bottom=-2000, top=2000)


plt.show()
'''

w = np.linspace(0, 2*np.pi*fs, duracion*fs, endpoint=None)
f = np.linspace(0, fs, duracion*fs, endpoint=None)

fig, axes = plt.subplots(2, 2)

axes[0][0].plot(w, re_X)
axes[0][0].set_xlabel("w (rad/s)")
axes[0][0].set_xticks(np.arange(500*np.pi, 2*np.pi*fs + 1, 500*np.pi))
axes[0][0].set_xticklabels([str(k) + 'π' for k in range(500, 2001, 500)])
axes[0][1].plot(f, re_X)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(w[0:int(len(w)/2)], re_X[0:int(len(re_X)/2)])
axes[1][0].set_xlabel("w (rad/s)")
axes[1][0].set_xticks(np.arange(500*np.pi, np.pi*fs + 1, 500*np.pi))
axes[1][0].set_xticklabels([str(k) + 'π' for k in range(500, 1001, 500)])
axes[1][1].plot(f[0:int(len(f)/2)], re_X[0:int(len(re_X)/2)])
axes[1][1].set_xlabel("f (Hz)")
axes[1][1].set_xticks(np.arange(0, fs/2 + 1, 100))
axes[1][1].set_xticklabels([str(k) for k in range(0, int(fs/2) + 1, 100)])

plt.show()