# Estados posibles
estados = ['Soleado', 'Lluvioso']

# Creencia inicial
creencia = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Modelo de transición P(X_t | X_{t-1})
transiciones = {
    'Soleado': {'Soleado': 0.7, 'Lluvioso': 0.3},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Modelo de observación P(evidencia | estado)
observaciones = {
    'Soleado': {'sombrilla': 0.2, 'no_sombrilla': 0.8},
    'Lluvioso': {'sombrilla': 0.9, 'no_sombrilla': 0.1}
}


def filtrar(creencia, evidencia):

    nueva_creencia = {}

    for s2 in estados:

        # Predicción (paso de tiempo)
        prob = 0
        for s in estados:
            prob += creencia[s] * transiciones[s][s2]

        # Corrección con evidencia
        prob *= observaciones[s2][evidencia]

        nueva_creencia[s2] = prob

    # Normalizar
    total = sum(nueva_creencia.values())
    for s in nueva_creencia:
        nueva_creencia[s] /= total

    return nueva_creencia


# Secuencia de observaciones
evidencias = ['sombrilla', 'sombrilla', 'no_sombrilla']

for e in evidencias:
    creencia = filtrar(creencia, e)
    print("Creencia:", creencia)