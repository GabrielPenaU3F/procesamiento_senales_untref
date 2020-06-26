import numpy as np
from matplotlib import pyplot as plt

from ejemplos.filtros.filtros_ideales import filtrar_pasa_bajos_ideal
from ejemplos.filtros.ruido.generador_ruido import generar_pico_de_ruido

# Filtrado pasa bajos de una señal cuadrada con un pico de ruido en 1kHz
from ejemplos.practica_4.funciones import generar_senal_cuadrada

fs = 44100
t, senal = generar_senal_cuadrada(0.5, 0, 4, fs)
N = len(senal)
espectro = np.abs(np.fft.fft(senal))[0:int(N/2)]


ruido = generar_pico_de_ruido(senal, fs, 1000, 20)
senal_ruidosa = senal + ruido
espectro_ruidoso = np.abs(np.fft.fft(senal_ruidosa))[0:int(N/2)]

senal_filtrada = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 800)
espectro_filtrado = np.abs(np.fft.fft(senal_filtrada))[0:int(N/2)]

f = np.linspace(0, fs/2, len(espectro_ruidoso), endpoint=None)

fig, axes = plt.subplots(3, 2)

axes[0][0].plot(t, senal)
axes[0][0].set_xlabel("t (seg)")

axes[0][1].plot(f, espectro)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(t, senal_ruidosa)
axes[1][0].set_xlabel("t (seg)")

axes[1][1].plot(f, espectro_ruidoso)
axes[1][1].set_xlabel("f (Hz)")

axes[2][0].plot(t, senal_filtrada)
axes[2][0].set_xlabel("t (seg)")

axes[2][1].plot(f, espectro_filtrado)
axes[2][1].set_xlabel("f (Hz)")

plt.show()
