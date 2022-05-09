import numpy as np


def calcular_transformada(x_t):
    X_w = np.fft.fft(x_t, norm='forward')
    return X_w

def poner_a_cero_valores_nulos(X_w, tol):
    max_x = max(np.abs(X_w))
    X_w_aux = []
    for k in range(len(X_w)):
        if np.abs(X_w[k])/max_x < tol:
            X_w_aux.append(complex(0, 0))
        else:
            X_w_aux.append(X_w[k])
    return X_w_aux
