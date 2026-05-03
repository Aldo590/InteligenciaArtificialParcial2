gamma = 0.9  # factor de descuento

# Estados
estados = ['A', 'B', 'C']

# Acciones disponibles
acciones = {
    'A': ['ir_B', 'ir_C'],
    'B': ['ir_C'],
    'C': []  # estado terminal
}

# Transiciones: (estado, acción) -> [(prob, siguiente_estado, recompensa)]
transiciones = {
    ('A', 'ir_B'): [(1.0, 'B', 5)],
    ('A', 'ir_C'): [(1.0, 'C', 10)],
    ('B', 'ir_C'): [(1.0, 'C', 2)]
}

# Política inicial (arbitraria)
politica = {
    'A': 'ir_B',
    'B': 'ir_C',
    'C': None
}

# Valores de los estados
V = {s: 0 for s in estados}


def evaluar_politica():
    # Aproximamos V(s) repitiendo varias veces
    for _ in range(10):
        nuevo_V = V.copy()

        for s in estados:

            # Si es terminal, no se actualiza
            if politica[s] is None:
                continue

            a = politica[s]  # acción fija según la política
            valor = 0

            # Calcula el valor esperado de esa acción
            for prob, s2, recompensa in transiciones[(s, a)]:
                valor += prob * (recompensa + gamma * V[s2])

            nuevo_V[s] = valor

        # Actualizamos todos los estados a la vez
        for s in estados:
            V[s] = nuevo_V[s]


def mejorar_politica():
    estable = True  # indica si la política deja de cambiar

    for s in estados:

        # Si no hay acciones, se ignora
        if s not in acciones or not acciones[s]:
            continue

        mejor_accion = None
        mejor_valor = float('-inf')

        # Probar todas las acciones posibles
        for a in acciones[s]:

            valor = 0

            # Evaluar cada acción usando V(s')
            for prob, s2, recompensa in transiciones[(s, a)]:
                valor += prob * (recompensa + gamma * V[s2])

            # Elegir la acción con mayor valor
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = a

        # Si cambia la acción, la política no es estable
        if politica[s] != mejor_accion:
            politica[s] = mejor_accion
            estable = False

    return estable


# Bucle principal
while True:

    evaluar_politica()      # calcula V(s) con la política actual

    if mejorar_politica():  # si ya no cambia, terminamos
        break


print("Valores finales:", V)
print("Política óptima:", politica)