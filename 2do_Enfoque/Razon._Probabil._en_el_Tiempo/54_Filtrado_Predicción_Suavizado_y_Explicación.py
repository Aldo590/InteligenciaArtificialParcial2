# Probabilidad inicial
P_inicial = {True: 0.5, False: 0.5}

# Transición: P(Xt | Xt-1)
P_transicion = {
    True:  {True: 0.7, False: 0.3},
    False: {True: 0.3, False: 0.7}
}

# Observación: P(et | Xt)
P_observacion = {
    True:  {True: 0.9, False: 0.1},   # si llueve
    False: {True: 0.2, False: 0.8}    # si no llueve
}


# -------------------------
# Normalización
# -------------------------
def normalizar(dist):
    total = sum(dist.values())
    for k in dist:
        dist[k] /= total
    return dist


# -------------------------
# FILTRADO
# P(Xt | e1...et)
# -------------------------
def filtrado(observaciones):

    belief = P_inicial.copy()  # creencia inicial

    for obs in observaciones:

        nuevo = {}

        for estado in [True, False]:

            # suma sobre estados anteriores (predicción)
            suma = 0
            for prev in [True, False]:
                suma += belief[prev] * P_transicion[prev][estado]

            # incorporar evidencia
            nuevo[estado] = suma * P_observacion[estado][obs]

        # normalizar
        belief = normalizar(nuevo)

    return belief


# -------------------------
# PREDICCIÓN
# P(Xt+k | e1...et)
# -------------------------
def prediccion(belief, pasos):

    for _ in range(pasos):

        nuevo = {}

        for estado in [True, False]:

            suma = 0
            for prev in [True, False]:
                suma += belief[prev] * P_transicion[prev][estado]

            nuevo[estado] = suma

        belief = normalizar(nuevo)

    return belief


# -------------------------
# SUAVIZADO (simple)
# P(Xk | e1...et)
# -------------------------
def suavizado(observaciones):

    # forward (filtrado)
    forward = []
    belief = P_inicial.copy()

    for obs in observaciones:
        nuevo = {}
        for estado in [True, False]:
            suma = 0
            for prev in [True, False]:
                suma += belief[prev] * P_transicion[prev][estado]
            nuevo[estado] = suma * P_observacion[estado][obs]

        belief = normalizar(nuevo)
        forward.append(belief.copy())

    # backward simplificado (solo ejemplo)
    return forward  # devuelve creencias en cada tiempo


# -------------------------
# EXPLICACIÓN (Viterbi)
# Secuencia más probable
# -------------------------
def viterbi(observaciones):

    V = [{}]       # tabla de probabilidades
    path = {}      # caminos

    # inicialización
    for estado in [True, False]:
        V[0][estado] = P_inicial[estado] * P_observacion[estado][observaciones[0]]
        path[estado] = [estado]

    # iteraciones
    for t in range(1, len(observaciones)):
        V.append({})
        new_path = {}

        for estado in [True, False]:

            # elegir mejor estado anterior
            prob, prev_estado = max(
                (V[t-1][prev] * P_transicion[prev][estado] * P_observacion[estado][observaciones[t]], prev)
                for prev in [True, False]
            )

            V[t][estado] = prob
            new_path[estado] = path[prev_estado] + [estado]

        path = new_path

    # elegir mejor camino final
    n = len(observaciones) - 1
    prob, estado = max((V[n][s], s) for s in [True, False])

    return path[estado]


# -------------------------
# Ejemplo
# -------------------------

observaciones = [True, True, False]  # paraguas observado

# Filtrado
f = filtrado(observaciones)
print("Filtrado:", f)

# Predicción (2 pasos al futuro)
p = prediccion(f, 2)
print("Predicción:", p)

# Suavizado
s = suavizado(observaciones)
print("Suavizado:", s)

# Explicación (Viterbi)
e = viterbi(observaciones)
print("Explicación:", e)