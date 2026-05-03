gamma = 0.9  # factor de descuento (importancia del futuro)

# Estados
estados = ['A', 'B', 'C']

# Acciones disponibles en cada estado
acciones = {
    'A': ['ir_B', 'ir_C'],
    'B': ['ir_C'],
    'C': []  # estado terminal
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

    nuevo_V = V.copy()  # copia para actualizar simultáneamente

    for s in estados:

        # Si el estado no tiene acciones, se considera terminal
        if s not in acciones or not acciones[s]:
            continue

        valores_acciones = []  # guarda el valor de cada acción

        # Evaluar cada acción posible
        for a in acciones[s]:

            valor = 0  # valor esperado de la acción

            # Evaluar posibles resultados de la acción
            for prob, s2, recompensa in transiciones[(s, a)]:

                # Fórmula de Bellman:
                # recompensa inmediata + valor futuro descontado
                valor += prob * (recompensa + gamma * V[s2])

            valores_acciones.append(valor)

        # Elegir la mejor acción (máximo valor)
        nuevo_V[s] = max(valores_acciones)

    # Actualizar todos los estados al mismo tiempo
    V = nuevo_V


# Mostrar valores finales
print("Valores de los estados:", V)


# Obtener política óptima
politica = {}

for s in estados:

    # Estados terminales no tienen acción
    if s not in acciones or not acciones[s]:
        politica[s] = None
        continue

    mejor_accion = None
    mejor_valor = float('-inf')

    # Evaluar todas las acciones para elegir la mejor
    for a in acciones[s]:

        valor = 0

        for prob, s2, recompensa in transiciones[(s, a)]:
            valor += prob * (recompensa + gamma * V[s2])

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_accion = a

    politica[s] = mejor_accion

print("Política óptima:", politica)