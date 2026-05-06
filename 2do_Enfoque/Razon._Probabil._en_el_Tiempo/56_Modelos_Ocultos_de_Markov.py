P_inicial = {True: 0.5, False: 0.5}

P_transicion = {
    True:  {True: 0.7, False: 0.3},
    False: {True: 0.3, False: 0.7}
}

P_observacion = {
    True:  {True: 0.9, False: 0.1},
    False: {True: 0.2, False: 0.8}
}



# Normalización

def normalizar(dist):
    total = sum(dist.values())
    for k in dist:
        dist[k] /= total
    return dist



# FORWARD (α)

def forward(observaciones):

    alpha = []

    # inicialización
    a0 = {}
    for estado in [True, False]:
        a0[estado] = P_inicial[estado] * P_observacion[estado][observaciones[0]]

    alpha.append(normalizar(a0))

    # iteraciones
    for t in range(1, len(observaciones)):

        at = {}

        for estado in [True, False]:

            suma = 0
            for prev in [True, False]:
                suma += alpha[t-1][prev] * P_transicion[prev][estado]

            at[estado] = suma * P_observacion[estado][observaciones[t]]

        alpha.append(normalizar(at))

    return alpha


# BACKWARD (β)

def backward(observaciones):

    T = len(observaciones)
    beta = [{} for _ in range(T)]

    # inicialización (último = 1)
    for estado in [True, False]:
        beta[T-1][estado] = 1

    # hacia atrás
    for t in reversed(range(T-1)):

        for estado in [True, False]:

            suma = 0
            for sig in [True, False]:
                suma += (
                    P_transicion[estado][sig] *
                    P_observacion[sig][observaciones[t+1]] *
                    beta[t+1][sig]
                )

            beta[t][estado] = suma

    return beta



# FORWARD-BACKWARD

def forward_backward(observaciones):

    alpha = forward(observaciones)
    beta = backward(observaciones)

    posterior = []

    for t in range(len(observaciones)):

        dist = {}

        for estado in [True, False]:
            # combinar α y β
            dist[estado] = alpha[t][estado] * beta[t][estado]

        posterior.append(normalizar(dist))

    return posterior



# Ejemplo


observaciones = [True, True, False]

resultado = forward_backward(observaciones)

print("P(Xt | evidencia):")
for t, r in enumerate(resultado):
    print(f"t={t}:", r)