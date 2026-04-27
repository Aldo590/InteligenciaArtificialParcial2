def haz_local(grafo, estados_iniciales, h, k=2, max_iter=10):

    # Estados actuales (k estados)
    actuales = estados_iniciales

    for _ in range(max_iter):

        todos_vecinos = []

        # Generar vecinos de todos los estados actuales
        for estado in actuales:
            for vecino in grafo[estado]:
                todos_vecinos.append(vecino)

        # Si no hay vecinos, terminar
        if not todos_vecinos:
            break

        # Ordenar vecinos según heurística (menor es mejor)
        todos_vecinos.sort(key=lambda x: h[x])

        # Seleccionar los k mejores
        actuales = todos_vecinos[:k]

        print("Estados actuales:", actuales)

    # Devolver el mejor de los actuales
    return min(actuales, key=lambda x: h[x])


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
    'D': 4,
    'E': 2,
    'F': 0
}

resultado = haz_local(grafo, ['A'], h, k=2)
print("Mejor encontrado:", resultado)