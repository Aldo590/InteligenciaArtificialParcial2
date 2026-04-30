# Estados posibles
estados = ['Soleado', 'Lluvioso']

# Creencia inicial (probabilidad de cada estado)
creencia = {
    'Soleado': 0.6,
    'Lluvioso': 0.4
}

# Modelo de transición: P(s' | s, acción)
transiciones = {
    ('Soleado', 'esperar'): {'Soleado': 0.7, 'Lluvioso': 0.3},
    ('Lluvioso', 'esperar'): {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Modelo de observación: P(observación | estado)
observaciones = {
    ('Soleado', 'nublado'): 0.2,
    ('Lluvioso', 'nublado'): 0.8
}


def actualizar_creencia(creencia, accion, observacion):

    nueva_creencia = {}

    for s2 in estados:

        prob = 0

        # Suma sobre estados anteriores
        for s in estados:

            prob += creencia[s] * transiciones[(s, accion)][s2]

        # Multiplicar por probabilidad de observación
        prob *= observaciones[(s2, observacion)]

        nueva_creencia[s2] = prob

    # Normalizar (para que sumen 1)
    total = sum(nueva_creencia.values())

    for s in nueva_creencia:
        nueva_creencia[s] /= total

    return nueva_creencia


# Ejemplo
accion = 'esperar'
observacion = 'nublado'

nueva_creencia = actualizar_creencia(creencia, accion, observacion)

print("Creencia actualizada:", nueva_creencia)