# Factores representados como diccionarios

# P(Nubes)
factor_nubes = {
    True: 0.5,
    False: 0.5
}

# P(Lluvia | Nubes)
factor_lluvia = {
    (True, True): 0.8,   # (nubes, lluvia)
    (True, False): 0.2,
    (False, True): 0.2,
    (False, False): 0.8
}

# P(Paraguas | Lluvia)
factor_paraguas = {
    (True, True): 0.9,   # (lluvia, paraguas)
    (True, False): 0.1,
    (False, True): 0.1,
    (False, False): 0.9
}


def eliminar_nubes(paraguas_evidencia=True):
    """
    Calcula P(lluvia | paraguas) eliminando variable 'nubes'
    """

    resultados = {}

    # variable de consulta: lluvia
    for lluvia in [True, False]:

        suma = 0

        # eliminar nubes (sumar sobre sus valores)
        for nubes in [True, False]:

            # obtener factores

            # P(nubes)
            P_N = factor_nubes[nubes]

            # P(lluvia | nubes)
            P_L = factor_lluvia[(nubes, lluvia)]

            # P(paraguas | lluvia)
            P_P = factor_paraguas[(lluvia, paraguas_evidencia)]

            # multiplicación de factores
            suma += P_N * P_L * P_P

        resultados[lluvia] = suma

    # normalización
    total = sum(resultados.values())
    for k in resultados:
        resultados[k] /= total

    return resultados


# Ejemplo

resultado = eliminar_nubes(True)

print("P(lluvia | paraguas):", resultado)