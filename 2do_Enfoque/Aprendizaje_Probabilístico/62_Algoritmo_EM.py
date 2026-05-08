import random


# Datos observados
datos = [1.0, 1.2, 0.8, 5.0, 5.2, 4.8]


# Parámetros iniciales
media1 = random.uniform(0, 6)
media2 = random.uniform(0, 6)

# Varianza fija simplificada
varianza = 1


# Función gaussiana simple
def gauss(x, media):

    return (1 / (2 * 3.1416 * varianza) ** 0.5) * \
           (2.71828 ** (-((x - media) ** 2) / (2 * varianza)))


# Algoritmo EM
def EM(iteraciones):

    global media1, media2

    for _ in range(iteraciones):

        # Paso E:
        # calcular responsabilidades
        responsabilidades = []

        for x in datos:

            # Probabilidad para cluster 1
            p1 = gauss(x, media1)

            # Probabilidad para cluster 2
            p2 = gauss(x, media2)

            # Normalización
            total = p1 + p2

            r1 = p1 / total
            r2 = p2 / total

            responsabilidades.append((r1, r2))

        # Paso M:
        # actualizar medias

        suma_r1 = 0
        suma_r2 = 0

        suma_x1 = 0
        suma_x2 = 0

        for i, x in enumerate(datos):

            r1, r2 = responsabilidades[i]

            suma_r1 += r1
            suma_r2 += r2

            suma_x1 += r1 * x
            suma_x2 += r2 * x

        # Nuevas medias
        media1 = suma_x1 / suma_r1
        media2 = suma_x2 / suma_r2

    return media1, media2


# Ejecutar EM
m1, m2 = EM(10)

print("Media 1:", m1)
print("Media 2:", m2)