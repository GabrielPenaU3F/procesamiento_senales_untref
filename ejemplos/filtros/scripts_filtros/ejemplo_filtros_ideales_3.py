import numpy as np
from matplotlib import pyplot as plt

from ejemplos.filtros.filtros_ideales import filtrar_pasa_bajos_ideal_fase_lineal
from ejemplos.filtros.ruido.generador_ruido import generar_pico_de_ruido
from ejemplos.practica_2.funciones import generar_senoide

# Filtrado pasa bajos con fase lineal de una señal con un pico de ruido en 16kHz
# El efecto del retardo de la fase lineal no se vé

fs = 44100
t, senal = generar_senoide(0, 4, 2, 440, 0, fs)
N = len(senal)

ruido = generar_pico_de_ruido(senal, fs, 16000, 20)
senal_ruidosa = senal + ruido
espectro_ruidoso = np.abs(np.fft.fft(senal_ruidosa))[0:int(N/2)]

senal_filtrada = filtrar_pasa_bajos_ideal_fase_lineal(senal_ruidosa, fs, 5000, 1)
espectro_filtrado = np.abs(np.fft.fft(senal_filtrada))[0:int(N/2)]

f = np.linspace(0, fs/2, len(espectro_ruidoso), endpoint=None)

fig, axes = plt.subplots(2, 2)

axes[0][0].plot(t, senal_ruidosa)
axes[0][0].set_xlabel("t (seg)")
axes[0][0].set_xlim(left=0, right=50/44100)

axes[0][1].plot(f, espectro_ruidoso)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(t, senal_filtrada)
axes[1][0].set_xlabel("t (seg)")
axes[1][0].set_xlim(left=0, right=50/44100)

axes[1][1].plot(f, espectro_filtrado)
axes[1][1].set_xlabel("f (Hz)")

plt.show()
