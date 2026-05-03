def hill_climbing(grafo, inicio, h):

    nodo_actual = inicio  # Nodo donde empezamos

    while True:
        vecinos = grafo[nodo_actual]  # Obtener vecinos

        # Si no hay vecinos, termina
        if not vecinos:
            return nodo_actual

        # Elegir el vecino con mejor heurística (menor valor)
        mejor_vecino = min(vecinos, key=lambda x: h[x])

        # Si no mejora, se detiene (óptimo local)
        if h[mejor_vecino] >= h[nodo_actual]:
            return nodo_actual

        # Moverse al mejor vecino
        nodo_actual = mejor_vecino


# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

h = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 2,
    'F': 0
}

resultado = hill_climbing(grafo, 'A', h)
print("Resultado:", resultado)