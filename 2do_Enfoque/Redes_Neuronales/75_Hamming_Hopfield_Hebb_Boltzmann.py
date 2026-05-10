# Patrones almacenados
patrones = [
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]


# Entrada
entrada = [1, 0, 1, 1]


# Distancia de Hamming
def distancia_hamming(a, b):

    diferencia = 0

    for x, y in zip(a, b):

        if x != y:
            diferencia += 1

    return diferencia


# Buscar patrón más cercano
mejor_patron = None
mejor_distancia = float("inf")

for patron in patrones:

    d = distancia_hamming(entrada, patron)

    if d < mejor_distancia:

        mejor_distancia = d
        mejor_patron = patron


print("Patrón reconocido:")
print(mejor_patron)