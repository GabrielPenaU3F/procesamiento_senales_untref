import numpy as np
from matplotlib import pyplot as plt

from ejemplos.practica_1.funciones import calcular_duracion, calcular_valor_medio_discreto

x = [-1, 1, -1, 0, 1, -1, 1, 0]
fs = 2

media = calcular_valor_medio_discreto(x)
print('Valor medio:' + str(media))

duracion = calcular_duracion(x, fs)
t = np.linspace(0, duracion, len(x), endpoint=None)
plt.stem(t, x)
plt.show()