import numpy as np


#  Nivel: debe pasarse una cantidad en dB. Define la relación señal-ruido (SNR)
from ejemplos.practica_2.funciones import calcular_potencia, generar_senoide

def generar_pico_de_ruido(senal, fs, frec_pico, snr):
    cantidad_muestras = len(senal)
    duracion = cantidad_muestras / fs
    potencia_media_senal = calcular_potencia(senal, fs)
    potencia_ruido_db = 10*np.log10(potencia_media_senal) - snr
    potencia_ruido = 10**(potencia_ruido_db/10)
    omega_2_L = 2 * 2 * np.pi * frec_pico * duracion
    amplitud_ruido = np.sqrt(potencia_ruido * 2 * omega_2_L / (omega_2_L + np.sin(omega_2_L)))
    t, ruido = generar_senoide(0, duracion, amplitud_ruido, frec_pico, 0, fs)
    return ruido

def generar_ruido_blanco(senal, fs, mu, sigma, snr):
    N = len(senal)
    ruido = np.random.normal(mu, sigma, N)
    potencia_media_senal = calcular_potencia(senal, fs)
    potencia_ruido_db_necesaria = 10 * np.log10(potencia_media_senal) - snr
    potencia_ruido_necesaria = 10 ** (potencia_ruido_db_necesaria / 10)
    potencia_ruido_real = calcular_potencia(ruido, fs)
    factor_amplitud = np.sqrt(potencia_ruido_necesaria / potencia_ruido_real)
    ruido = ruido * factor_amplitud
    return ruido

def generar_ruido_sal_y_pimienta(senal, fs, p, snr):
    N = len(senal)
    ruido = np.random.binomial(1, p, N)
    potencia_media_senal = calcular_potencia(senal, fs)
    potencia_ruido_db_necesaria = 10 * np.log10(potencia_media_senal) - snr
    potencia_ruido_necesaria = 10 ** (potencia_ruido_db_necesaria / 10)
    potencia_ruido_real = calcular_potencia(ruido, fs)
    factor_amplitud = np.sqrt(potencia_ruido_necesaria / potencia_ruido_real)
    ruido = ruido * factor_amplitud
    return ruido