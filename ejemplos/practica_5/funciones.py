import scipy


def calcular_transformada(x_t):
    X_w = scipy.fft.fft(x_t)
    return X_w