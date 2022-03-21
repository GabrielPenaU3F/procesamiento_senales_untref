import numpy as np

from ejemplos.practica_1.funciones import calcular_duracion
from matplotlib import pyplot as plt

y = [3, 1, 2, 1, 0, -1, 2, 1, 0, 1]
fs = 2

# 10 muestras, 2 por unidad de tiempo

print(calcular_duracion(y, fs))

# t = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
t = np.linspace(0, 5, len(y), endpoint=None)

markerline, stemlines, baseline = plt.stem(t, y, linefmt='--', markerfmt='o', basefmt='black', label='y(t)')
plt.setp(markerline, 'color', '#A00C00')
plt.setp(stemlines, 'color', 'blue')
plt.grid()
plt.legend()
plt.show()
