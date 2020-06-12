import numpy as np


def estan_afinadas(x, y, fs, tol_abs):

    N_x = len(x)
    N_y = len(y)

    x_fft = np.abs(np.fft.fft(x))[0:int(N_x/2)]
    y_fft = np.abs(np.fft.fft(y))[0:int(N_y/2)]

    indice_maximo_x = np.argmax(x_fft)
    indice_maximo_y = np.argmax(y_fft)

    f_max_x = float(indice_maximo_x * fs) / float(N_x)
    f_max_y = float(indice_maximo_y * fs) / float(N_y)

    condicion = abs(f_max_x - f_max_y) < tol_abs

    return condicion
