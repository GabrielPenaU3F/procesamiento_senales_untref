import numpy as np
from matplotlib import pyplot as plt

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


