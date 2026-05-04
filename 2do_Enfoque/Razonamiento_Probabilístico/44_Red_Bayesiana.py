# Probabilidades a priori
P_nubes = 0.5

# Probabilidad de lluvia dado nubes
P_lluvia_dado_nubes = {
    True: 0.8,
    False: 0.2
}

# Probabilidad de paraguas dado lluvia
P_paraguas_dado_lluvia = {
    True: 0.9,
    False: 0.1
}


def inferencia_paraguas():
    """
    Calcula P(paraguas) sumando sobre nubes y lluvia
    """

    total = 0

    # Iterar sobre posibles valores de nubes
    for nubes in [True, False]:

        # Probabilidad de nubes
        P_N = P_nubes if nubes else (1 - P_nubes)

        # Iterar sobre lluvia
        for lluvia in [True, False]:

            # P(lluvia | nubes)
            if lluvia:
                P_L = P_lluvia_dado_nubes[nubes]
            else:
                P_L = 1 - P_lluvia_dado_nubes[nubes]

            # P(paraguas | lluvia)
            P_P = P_paraguas_dado_lluvia[lluvia]

            # Regla del producto
            total += P_N * P_L * P_P

    return total


resultado = inferencia_paraguas()

print("P(paraguas) =", resultado)