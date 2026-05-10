# Datos de ejemplo
datos = [2, 3, 4, 10, 11, 12]


# Algoritmo simple de clustering
def clustering(datos):

    grupo1 = []
    grupo2 = []

    for x in datos:

        # Separación simple por valor
        if x < 7:
            grupo1.append(x)
        else:
            grupo2.append(x)

    return grupo1, grupo2


# Ejecutar clustering
g1, g2 = clustering(datos)

print("Cluster 1:", g1)
print("Cluster 2:", g2)