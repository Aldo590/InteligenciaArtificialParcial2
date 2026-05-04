# Probabilidades base
P_nubes = 0.5

P_lluvia_dado_nubes = {
    True: 0.8,
    False: 0.2
}

P_paraguas_dado_lluvia = {
    True: 0.9,
    False: 0.1
}


# Función para calcular probabilidad conjunta
def probabilidad_conjunta(nubes, lluvia, paraguas):

    # P(nubes)
    P_N = P_nubes if nubes else (1 - P_nubes)

    # P(lluvia | nubes)
    P_L = P_lluvia_dado_nubes[nubes] if lluvia else (1 - P_lluvia_dado_nubes[nubes])

    # P(paraguas | lluvia)
    P_P = P_paraguas_dado_lluvia[lluvia] if paraguas else (1 - P_paraguas_dado_lluvia[lluvia])

    # Regla de la cadena
    return P_N * P_L * P_P


def inferencia_paraguas(evidencia_paraguas=True):
    """
    Calcula P(lluvia | paraguas)
    """

    resultados = {}

    # Variable de consulta: lluvia
    for lluvia in [True, False]:

        suma = 0

        # Enumerar variable oculta: nubes
        for nubes in [True, False]:

            # calcular P(nubes, lluvia, paraguas)
            suma += probabilidad_conjunta(nubes, lluvia, evidencia_paraguas)

        resultados[lluvia] = suma

    # Normalización
    total = sum(resultados.values())

    for k in resultados:
        resultados[k] /= total

    return resultados


# Ejemplo

resultado = inferencia_paraguas(True)

print("P(lluvia | paraguas):", resultado)