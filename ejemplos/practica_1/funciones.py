import numpy as np


def calcular_duracion(y, fs):
    periodo_muestral = 1 / fs
    duracion = periodo_muestral * len(y)
    return duracion


def calcular_valor_medio_discreto(x):
   return (1 / len(x)) * np.sum(x)
