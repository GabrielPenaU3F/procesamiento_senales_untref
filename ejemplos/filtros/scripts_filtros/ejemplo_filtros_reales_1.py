import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as sg

from ejemplos.filtros.filtros_ideales import filtrar_pasa_bajos_ideal
from ejemplos.filtros.ruido.generador_ruido import generar_pico_de_ruido
from ejemplos.practica_4.funciones import generar_senal_cuadrada

# Filtrado pasa bajos de una señal cuadrada con un pico de ruido en 1kHz

fs = 44100
t, senal = generar_senal_cuadrada(0.5, 0, 4, fs)
N = len(senal)
espectro = np.abs(np.fft.fft(senal))[0:int(N/2)]

ruido = generar_pico_de_ruido(senal, fs, 1000, 10)
senal_ruidosa = senal + ruido
espectro_ruidoso = np.abs(np.fft.fft(senal_ruidosa))[0:int(N/2)]

fpass = 800
fstop = 950
wpass = 800 / (fs/2)
wstop = 950 / (fs/2)

# Las frecuencias angulares fpass y fstop se tienen que normalizar al intervalo (0, 1), donde 1 corresponde
# a la frecuencia de Nyquist (fs / 2). Para eso dividimos por (fs/2)

orden, wn = sg.cheb1ord(wp=wpass, ws=wstop, gpass=3, gstop=40)
[coef_numerador_b, coef_denominador_a] = sg.cheby1(N=orden, rp=3, Wn=wn, btype='lowpass', output='ba')

''' Diagrama de Bode '''

# Le pasamos la frecuencia de muestreo para que el resultado lo ponga en escala de 0 a fs/2
f, h = sg.freqz(coef_numerador_b, coef_denominador_a, fs=fs)

fig, ax1 = plt.subplots()
ax1.set_title('Filtro Chebyshev Tipo I pasa bajos')

ax1.plot(f, 20 * np.log10(abs(h)))
ax1.set_xlabel('Frecuencia [Hz]')
ax1.set_ylabel('Amplitud [dB]')
ax1.margins(0, 0.1)
ax1.grid(which='both', axis='both')

ax2 = ax1.twinx()
ax2.plot(f, np.unwrap(np.angle(h)), 'g')
ax2.set_ylabel('Fase (rad)', color='g')

senal_filtrada_ideal = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 800)
espectro_filtrado_ideal = np.abs(np.fft.fft(senal_filtrada_ideal))[0:int(N/2)]

senal_filtrada_butterworth = sg.lfilter(coef_numerador_b, coef_denominador_a, senal_ruidosa)
espectro_filtrado_butterworth = np.abs(np.fft.fft(senal_filtrada_butterworth))[0:int(N/2)]


f = np.linspace(0, fs/2, len(espectro_ruidoso), endpoint=None)

fig2, axes = plt.subplots(3, 2)

axes[0][0].plot(t, senal_ruidosa)
axes[0][0].set_xlabel("t (seg)")

axes[0][1].plot(f, espectro_ruidoso)
axes[0][1].set_xlabel("f (Hz)")

axes[1][0].plot(t, senal_filtrada_ideal)
axes[1][0].set_xlabel("t (seg)")

axes[1][1].plot(f, espectro_filtrado_ideal)
axes[1][1].set_xlabel("f (Hz)")

axes[2][0].plot(t, senal_filtrada_butterworth)
axes[2][0].set_xlabel("t (seg)")

axes[2][1].plot(f, espectro_filtrado_butterworth)
axes[2][1].set_xlabel("f (Hz)")


plt.show()
