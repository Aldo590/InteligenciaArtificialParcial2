import heapq  # Para manejar la cola de prioridad

def busqueda_heuristica(grafo, inicio, objetivo, h):

    # Cola de prioridad: (heurística, nodo)
    frontera = []
    heapq.heappush(frontera, (h[inicio], inicio))

    visitados = set()  # Nodos ya visitados

    while frontera:
        # Extrae el nodo con menor heurística
        _, nodo_actual = heapq.heappop(frontera)

        print(nodo_actual, end=" ")

        # Si es el objetivo, termina
        if nodo_actual == objetivo:
            return True

        # Si no ha sido visitado
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Agregar vecinos a la cola
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    heapq.heappush(frontera, (h[vecino], vecino))

    return False


# 🔹 Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heurística (estimación al objetivo F)
h = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 2,
    'F': 0
}

busqueda_heuristica(grafo, 'A', 'F', h)