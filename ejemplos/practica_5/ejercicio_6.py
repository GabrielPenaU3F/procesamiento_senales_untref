
from matplotlib import pyplot as plt
import numpy as np

from ejemplos.practica_2.funciones import generar_senoide
from ejemplos.practica_5.funciones import calcular_transformada, poner_a_cero_valores_nulos

fs = 500
ti = 0
tf = 5

t1, x1 = generar_senoide(ti, tf, 5, 50, 0, fs)
t2, x2 = generar_senoide(ti, tf, 3, 100, 0, fs)
t3, x3 = generar_senoide(ti, tf, 1, 200, 0, fs)

x = x1 + x2 + x3

duracion = tf - ti

X_w = calcular_transformada(x1)
X_w_aux = poner_a_cero_valores_nulos(X_w, 0.01)

mod_X = np.abs(X_w)[0:int(len(X_w)/2)]/(len(X_w)/2)
fase_X = np.angle(X_w)[0:int(len(X_w)/2)]

mod_X_aux = np.abs(X_w_aux)[0:int(len(X_w_aux)/2)]/(len(X_w_aux)/2)
fase_X_aux = np.angle(X_w_aux)[0:int(len(X_w_aux)/2)]

f = np.linspace(0, fs, duracion*fs, endpoint=None)[0:int(len(X_w)/2)]

fig, axes = plt.subplots(2, 2)

axes[0][0].plot(f, mod_X)
axes[0][0].set_xlabel("f (Hz)")

axes[0][1].plot(f, fase_X)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(f, mod_X_aux)
axes[1][0].set_xlabel("f (Hz)")

axes[1][1].plot(f, fase_X_aux)
axes[1][1].set_xlabel("f (Hz)")

plt.show()
