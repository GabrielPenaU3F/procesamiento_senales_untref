import scipy.signal as sg


def construir_kernel_media_movil(ancho_ventana):
    valor = 1/ancho_ventana
    kernel = []
    for k in range(ancho_ventana):
        kernel.append(valor)

    return kernel


kernel_ancho_5 = construir_kernel_media_movil(3)
x_t = [1, 3, 1, 2, 2, 1]

print(sg.convolve(x_t, kernel_ancho_5))