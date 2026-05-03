def distribucion_probabilidad(datos):
    """
    datos: lista de valores (ej. ['sol', 'lluvia', ...])
    """

    conteo = {}              # guarda frecuencia de cada valor
    total = len(datos)       # número total de datos

    # contar ocurrencias
    for d in datos:
        if d in conteo:
            conteo[d] += 1
        else:
            conteo[d] = 1

    # convertir a probabilidades
    distribucion = {}

    for valor in conteo:
        distribucion[valor] = conteo[valor] / total

    return distribucion


# Ejemplo

datos = [
    'sol', 'lluvia', 'sol', 'nublado',
    'sol', 'lluvia', 'sol'
]

resultado = distribucion_probabilidad(datos)

print("Distribución:", resultado)