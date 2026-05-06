import numpy as np

def verificar_estacionariedad(datos, segmentos=3):
    """
    Verifica si una serie es aproximadamente estacionaria
    comparando media y varianza en segmentos
    """

    datos = np.array(datos)

    # dividir en segmentos
    partes = np.array_split(datos, segmentos)

    medias = []
    varianzas = []

    for p in partes:
        medias.append(np.mean(p))       # media de cada segmento
        varianzas.append(np.var(p))     # varianza de cada segmento

    # comparar diferencias
    dif_media = max(medias) - min(medias)
    dif_var = max(varianzas) - min(varianzas)

    # umbrales simples
    if dif_media < 0.1 and dif_var < 0.1:
        return True
    else:
        return False


# Ejemplo

# Serie aproximadamente estacionaria
datos = [1, 2, 1, 2, 1, 2, 1, 2]

resultado = verificar_estacionariedad(datos)

print("¿Es estacionario?:", resultado)