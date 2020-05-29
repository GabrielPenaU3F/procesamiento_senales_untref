import numpy as np
from matplotlib import pyplot as plt

# s(t)= 2cos(2 pi t)
def generar_senoide(t_inicial, t_final, f, fs):
    cantidad_muestras = (t_final - t_inicial) * fs
    eje_t = np.linspace(t_inicial, t_final, cantidad_muestras, endpoint=False)
    senoide = []
    for k in range(len(eje_t)):
        senoide.append(2 * np.cos(2 * np.pi * f * eje_t[k]))
    return eje_t, np.array(senoide)

def calcular_energia(senoide, fs):
    energia = 0
    ts = 1/fs
    for k in range(len(senoide)):
        energia += (np.abs(senoide[k])**2)
    return energia * ts

# SCRIPT

'''

fs_10 = 10
fs_100 = 100
fs_1000 = 1000

t_inicial = 0
t_final = 1

t_10, senoide_10 = generar_senoide(t_inicial, t_final, 1, fs_10)
t_100, senoide_100 = generar_senoide(t_inicial, t_final, 1, fs_100)
t_1000, senoide_1000 = generar_senoide(t_inicial, t_final, 1, fs_1000)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(t_10, senoide_10)
ax2.plot(t_100, senoide_100)
ax3.plot(t_1000, senoide_1000)

e_10 = calcular_energia(senoide_10, fs_10)
e_100 = calcular_energia(senoide_100, fs_100)
e_1000 = calcular_energia(senoide_1000, fs_1000)

print('Energia (10 muestras por segundo): ' + str(e_10))
print('Energia (100 muestras por segundo): ' + str(e_100))
print('Energia (1000 muestras por segundo): ' + str(e_1000))

plt.show()

'''


