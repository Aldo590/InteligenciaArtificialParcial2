gamma = 0.9  # factor de descuento (qué tanto importa el futuro)

# Estados del problema
estados = ['A', 'B', 'C']

# Acciones disponibles en cada estado
acciones = {
    'A': ['ir_B', 'ir_C'],
    'B': ['ir_C'],
    'C': []  # estado terminal (no tiene acciones)
}

# Transiciones:
# (estado, acción) -> [(probabilidad, siguiente_estado, recompensa)]
transiciones = {
    ('A', 'ir_B'): [(1.0, 'B', 5)],
    ('A', 'ir_C'): [(1.0, 'C', 10)],
    ('B', 'ir_C'): [(1.0, 'C', 2)]
}

# Inicializar valores de los estados en 0
V = {s: 0 for s in estados}

# Iteración de valores
for _ in range(10):  # número de iteraciones (aproximación)

    nuevo_V = V.copy()  # copia para actualizar después

    for s in estados:

        # Si no hay acciones (estado terminal), se deja igual
        if s not in acciones or not acciones[s]:
            continue

        valores_acciones = []  # guarda valor de cada acción

        # Evaluar cada acción posible
        for a in acciones[s]:

            valor = 0  # valor esperado de la acción

            # Evaluar resultados de la acción
            for prob, s2, recompensa in transiciones[(s, a)]:

                # valor = recompensa inmediata + valor futuro descontado
                valor += prob * (recompensa + gamma * V[s2])

            valores_acciones.append(valor)

        # Elegir la mejor acción (la de mayor valor)
        nuevo_V[s] = max(valores_acciones)

    V = nuevo_V


#  Mostrar valores finales
print("Valores finales:", V)
