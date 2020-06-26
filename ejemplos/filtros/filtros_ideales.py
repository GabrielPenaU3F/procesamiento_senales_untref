import numpy as np


def filtrar_pasa_bajos_ideal(senal, fs, frec_corte):
    senal_fft = np.fft.fft(senal)
    senal_filtrada_fft = []
    muestra_corte = int(frec_corte * len(senal) / fs)
    for k in range(0, int(len(senal)/2)):
        if k > muestra_corte:
            senal_filtrada_fft.append(complex(0, 0))
        else:
            senal_filtrada_fft.append(senal_fft[k])

    for k in range(int(len(senal)/2), len(senal)):
        if k < len(senal) - muestra_corte:
            senal_filtrada_fft.append(complex(0, 0))
        else:
            senal_filtrada_fft.append(senal_fft[k])

    senal_filtrada = np.fft.ifft(senal_filtrada_fft)
    return senal_filtrada

def filtrar_pasa_bajos_ideal_fase_lineal(senal, fs, frec_corte, retardo):
    senal_fft = np.fft.fft(senal)
    senal_filtrada_fft = []
    muestra_corte = int(frec_corte * len(senal) / fs)
    for k in range(0, int(len(senal)/2)):
        if k > muestra_corte:
            senal_filtrada_fft.append(complex(0, 0))
        else:
            frec = k * fs / len(senal)
            omega = 2 * np.pi * frec
            muestra_filtrada = senal_fft[k] * np.exp(-retardo*1j*omega)
            senal_filtrada_fft.append(muestra_filtrada)

    for k in range(int(len(senal)/2),  len(senal)):
        if k < len(senal) - muestra_corte:
            senal_filtrada_fft.append(complex(0, 0))
        else:
            frec = k * fs / len(senal)
            omega = 2 * np.pi * frec
            muestra_filtrada = senal_fft[k] * np.exp(-retardo*1j*omega)
            senal_filtrada_fft.append(muestra_filtrada)

    senal_filtrada = np.fft.ifft(senal_filtrada_fft)
    return senal_filtrada