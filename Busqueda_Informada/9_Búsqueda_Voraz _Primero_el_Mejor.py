import heapq  # Permite usar una cola de prioridad

def voraz(grafo, inicio, objetivo, h):

    # Siempre se extrae el nodo con menor h(n)
    frontera = []
    heapq.heappush(frontera, (h[inicio], inicio))

    # Conjunto para no repetir nodos ya explorados
    visitados = set()

    # Mientras haya nodos por explorar
    while frontera:

        # Extrae el nodo con menor heurística
        heuristica_actual, nodo_actual = heapq.heappop(frontera)

        print(nodo_actual, end=" ")  # Mostrar recorrido (opcional)

        # Si llegamos al objetivo, termina la búsqueda
        if nodo_actual == objetivo:
            return True

        # Solo procesar si no ha sido visitado antes
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # Explorar todos los vecinos del nodo actual
            for vecino in grafo[nodo_actual]:

                # Evitar meter nodos ya visitados
                if vecino not in visitados:

                    # Insertar vecino con su valor heuristico
                    # Esto determina la prioridad en la cola
                    heapq.heappush(frontera, (h[vecino], vecino))

    # Si se vacía la frontera sin encontrar el objetivo
    return False


# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heuristica: estimacion de distancia al objetivo F
h = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 2,
    'F': 0
}

voraz(grafo, 'A', 'F', h)