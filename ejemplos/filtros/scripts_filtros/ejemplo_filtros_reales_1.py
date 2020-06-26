import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as sg

from ejemplos.filtros.filtros_ideales import filtrar_pasa_bajos_ideal
from ejemplos.filtros.ruido.generador_ruido import generar_pico_de_ruido

# Filtrado pasa bajos de una señal cuadrada con un pico de ruido en 1kHz
from ejemplos.practica_4.funciones import generar_senal_cuadrada

fs = 44100
t, senal = generar_senal_cuadrada(0.5, 0, 4, fs)
N = len(senal)
espectro = np.abs(np.fft.fft(senal))[0:int(N/2)]

ruido = generar_pico_de_ruido(senal, fs, 1000, 10)
senal_ruidosa = senal + ruido
espectro_ruidoso = np.abs(np.fft.fft(senal_ruidosa))[0:int(N/2)]

fpass = 800
fstop = 950
wpass = fpass * 2 / fs
wstop = fstop * 2 / fs
orden, wn = sg.buttord(wp=wpass, ws=wstop, gpass=1, gstop=40, fs=fs)
filtro = sg.butter(N=orden, Wn=wn, btype='lowpass', output='ba')
coef_numerador_b = filtro[0]
coef_denominador_a = filtro[1]

''' Diagrama de Bode '''

w, h = sg.freqz(coef_numerador_b, coef_denominador_a)
plt.plot(w/(2*np.pi), 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green') # cutoff frequency
plt.show()


'''
senal_filtrada_ideal = filtrar_pasa_bajos_ideal(senal_ruidosa, fs, 800)
espectro_filtrado_ideal = np.abs(np.fft.fft(senal_filtrada_ideal))[0:int(N/2)]

senal_filtrada_butterworth = sg.lfilter(coef_numerador_b, coef_denominador_a, senal_ruidosa)
espectro_filtrado_butterworth = np.abs(np.fft.fft(senal_filtrada_butterworth))[0:int(N/2)]


f = np.linspace(0, fs/2, len(espectro_ruidoso), endpoint=None)

fig, axes = plt.subplots(3, 2)

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
'''

plt.show()
