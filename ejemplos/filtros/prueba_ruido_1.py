import numpy as np

from ejemplos.filtros.generador_ruido import generar_pico_de_ruido
from ejemplos.practica_2.funciones import generar_senoide
from matplotlib import pyplot as plt

fs = 44100

t, senal = generar_senoide(0, 4, 2, 440, 0, fs)
N = len(senal)
espectro = np.abs(np.fft.fft(senal))[0:int(N/2)]

ruido = generar_pico_de_ruido(senal, fs, 16000, 20)
espectro_ruido = np.abs(np.fft.fft(ruido))[0:int(N/2)]

senal_ruidosa = senal + ruido
espectro_ruidoso = np.abs(np.fft.fft(senal_ruidosa))[0:int(N/2)]

f = np.linspace(0, fs/2, len(espectro), endpoint=None)

fig, axes = plt.subplots(3, 2)

axes[0][0].plot(t, senal)
axes[0][0].set_xlabel("t (seg)")
axes[0][0].set_xlim(left=0, right=50/44100)

axes[0][1].plot(f, espectro)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(t, ruido)
axes[1][0].set_xlabel("t (seg)")
axes[1][0].set_xlim(left=0, right=50/44100)

axes[1][1].plot(f, espectro_ruido)
axes[1][1].set_xlabel("f (Hz)")

axes[2][0].plot(t, senal_ruidosa)
axes[2][0].set_xlabel("t (seg)")
axes[2][0].set_xlim(left=0, right=50/44100)

axes[2][1].plot(f, espectro_ruidoso)
axes[2][1].set_xlabel("f (Hz)")

plt.show()
