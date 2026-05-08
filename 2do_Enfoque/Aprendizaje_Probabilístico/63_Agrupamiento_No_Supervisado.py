# Definición:
# El agrupamiento no supervisado (clustering)
# agrupa datos similares sin usar etiquetas.

import random


# Datos de ejemplo
datos = [1, 2, 1.5, 8, 9, 8.5]


# Inicializar centroides aleatorios
centroide1 = random.choice(datos)
centroide2 = random.choice(datos)


# Calcular distancia simple
def distancia(a, b):
    return abs(a - b)


# Algoritmo de agrupamiento tipo K-Means
def clustering(iteraciones):

    global centroide1, centroide2

    for _ in range(iteraciones):

        grupo1 = []
        grupo2 = []

        # Asignar datos al centroide más cercano
        for x in datos:

            d1 = distancia(x, centroide1)
            d2 = distancia(x, centroide2)

            if d1 < d2:
                grupo1.append(x)
            else:
                grupo2.append(x)

        # Actualizar centroides
        if len(grupo1) > 0:
            centroide1 = sum(grupo1) / len(grupo1)

        if len(grupo2) > 0:
            centroide2 = sum(grupo2) / len(grupo2)

    return grupo1, grupo2


# Ejecutar clustering
g1, g2 = clustering(10)

print("Grupo 1:", g1)
print("Grupo 2:", g2)

print("Centroide 1:", centroide1)
print("Centroide 2:", centroide2)