from ejemplos.practica_2.funciones import generar_senoide
import numpy as np
from matplotlib import pyplot as plt

t, x = generar_senoide(0, 3, 2, 50, 0, 44100)
t, y = generar_senoide(0, 3, 2, 50, np.pi, 44100)

z1 = x + y
z2 = x + (-x)

plt.plot(t, z1)
plt.show()

