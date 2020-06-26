import numpy as np
from matplotlib import pyplot as plt

from ejemplos.filtros.filtros_ideales import filtrar_pasa_bajos_ideal
from ejemplos.filtros.ruido.generador_ruido import generar_ruido_blanco
from ejemplos.practica_2.funciones import generar_senoide

# Filtrado pasa bajos de una señal con ruido blanco

fs = 44100
t, senal = generar_senoide(0, 4, 2, 440, 0, fs)
N = len(senal)
espectro = np.abs(np.fft.fft(senal))[0:int(N/2)]

ruido = generar_ruido_blanco(senal, fs, 0, 10, 0)
senal_ruidosa = senal + ruido
espectro_ruidoso = np.abs(np.fft.fft(senal_ruidosa))[0:int(N/2)]

senal_filtrada_5000 = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 5000)
espectro_filtrado_5000 = np.abs(np.fft.fft(senal_filtrada_5000))[0:int(N/2)]

senal_filtrada_2000 = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 2000)
espectro_filtrado_2000 = np.abs(np.fft.fft(senal_filtrada_5000))[0:int(N/2)]

senal_filtrada_1000 = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 1000)
espectro_filtrado_1000 = np.abs(np.fft.fft(senal_filtrada_5000))[0:int(N/2)]

senal_filtrada_500 = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 500)
espectro_filtrado_500 = np.abs(np.fft.fft(senal_filtrada_5000))[0:int(N/2)]

f = np.linspace(0, fs/2, len(espectro_ruidoso), endpoint=None)

fig, axes = plt.subplots(3, 4)

axes[0][0].plot(t, senal)
axes[0][0].set_xlabel("t (seg)")
axes[0][0].set_xlim(left=0, right=50/44100)

axes[0][1].plot(f, espectro)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(t, senal_ruidosa)
axes[1][0].set_xlabel("t (seg)")
axes[1][0].set_xlim(left=0, right=50/44100)

axes[1][1].plot(f, espectro_ruidoso)
axes[1][1].set_xlabel("f (Hz)")

axes[2][0].plot(t, senal_filtrada_5000)
axes[2][0].set_xlabel("t (seg)")
axes[2][0].set_xlim(left=0, right=50/44100)

axes[2][1].plot(f, espectro_filtrado_5000)
axes[2][1].set_xlabel("f (Hz)")

axes[0][2].plot(t, senal_filtrada_2000)
axes[0][2].set_xlabel("t (seg)")
axes[0][2].set_xlim(left=0, right=50/44100)

axes[0][3].plot(f, espectro_filtrado_2000)
axes[0][3].set_xlabel("f (Hz)")

axes[1][2].plot(t, senal_filtrada_1000)
axes[1][2].set_xlabel("t (seg)")
axes[1][2].set_xlim(left=0, right=50/44100)

axes[1][3].plot(f, espectro_filtrado_1000)
axes[1][3].set_xlabel("f (Hz)")

axes[2][2].plot(t, senal_filtrada_500)
axes[2][2].set_xlabel("t (seg)")
axes[2][2].set_xlim(left=0, right=50/44100)

axes[2][3].plot(f, espectro_filtrado_500)
axes[2][3].set_xlabel("f (Hz)")


plt.show()
