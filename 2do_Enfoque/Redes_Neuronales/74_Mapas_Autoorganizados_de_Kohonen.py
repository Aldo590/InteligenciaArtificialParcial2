import random
import math


# Datos de entrada
datos = [
    [1, 1],
    [1, 2],
    [2, 1],
    [8, 8],
    [9, 8],
    [8, 9]
]


# Inicializar neuronas
neuronas = [
    [random.uniform(0, 10), random.uniform(0, 10)]
    for _ in range(2)
]


# Tasa de aprendizaje
lr = 0.5


# Distancia euclidiana
def distancia(a, b):

    suma = 0

    for x, y in zip(a, b):

        suma += (x - y) ** 2

    return math.sqrt(suma)


# Entrenamiento SOM
for epoch in range(100):

    for dato in datos:

        mejor_neurona = 0
        mejor_distancia = float("inf")

        # Buscar neurona ganadora
        for i in range(len(neuronas)):

            d = distancia(dato, neuronas[i])

            if d < mejor_distancia:

                mejor_distancia = d
                mejor_neurona = i

        # Ajustar neurona ganadora
        for j in range(len(dato)):

            neuronas[mejor_neurona][j] += (
                lr * (dato[j] - neuronas[mejor_neurona][j])
            )


# Mostrar neuronas finales
print("Neuronas entrenadas:")

for n in neuronas:

    print(n)