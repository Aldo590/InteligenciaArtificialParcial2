# Implementación de la Regla de Bayes

def regla_de_bayes(P_A, P_B_dado_A, P_B_dado_noA):
    """
    P_A: probabilidad a priori de A
    P_B_dado_A: probabilidad de B si ocurre A
    P_B_dado_noA: probabilidad de B si no ocurre A
    """

    # Probabilidad de no A
    P_noA = 1 - P_A

    # Calcular P(B) usando probabilidad total
    P_B = (P_B_dado_A * P_A) + (P_B_dado_noA * P_noA)

    # Evitar división entre cero
    if P_B == 0:
        return 0

    # Aplicar fórmula de Bayes
    P_A_dado_B = (P_B_dado_A * P_A) / P_B

    return P_A_dado_B


# Ejemplo de uso

# Probabilidad de lluvia
P_lluvia = 0.3

# Probabilidad de ver paraguas si llueve
P_paraguas_dado_lluvia = 0.9

# Probabilidad de ver paraguas si no llueve
P_paraguas_dado_no_lluvia = 0.2

resultado = regla_de_bayes(
    P_lluvia,
    P_paraguas_dado_lluvia,
    P_paraguas_dado_no_lluvia
)

print("P(lluvia | paraguas) =", resultado)