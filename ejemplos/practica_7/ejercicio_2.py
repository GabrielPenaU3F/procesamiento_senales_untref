import numpy as np

from ejemplos.practica_2.funciones import generar_senoide
from ejemplos.practica_7.funciones import estan_afinadas

fs = 44100
t1, x = generar_senoide(0, 3, 2, 50, 0, fs)
t2, y = generar_senoide(1, 8, 10, 50.5, np.pi, fs)
tol_abs = 0.6

print(estan_afinadas(x, y, fs, tol_abs))
