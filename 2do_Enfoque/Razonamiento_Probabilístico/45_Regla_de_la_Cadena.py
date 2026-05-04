# Probabilidades dadas
P_A = 0.5

# P(B | A)
P_B_dado_A = {
    True: 0.7,
    False: 0.2
}

# P(C | A, B)
P_C_dado_A_B = {
    (True, True): 0.9,
    (True, False): 0.5,
    (False, True): 0.6,
    (False, False): 0.1
}


def regla_cadena(A, B, C):
    """
    Calcula P(A, B, C) usando la regla de la cadena
    """

    # P(A)
    P1 = P_A if A else (1 - P_A)

    # P(B | A)
    if B:
        P2 = P_B_dado_A[A]
    else:
        P2 = 1 - P_B_dado_A[A]

    # P(C | A, B)
    if C:
        P3 = P_C_dado_A_B[(A, B)]
    else:
        P3 = 1 - P_C_dado_A_B[(A, B)]

    # Regla de la cadena
    return P1 * P2 * P3


# Ejemplo: P(A=True, B=True, C=True)
resultado = regla_cadena(True, True, True)

print("P(A,B,C) =", resultado)