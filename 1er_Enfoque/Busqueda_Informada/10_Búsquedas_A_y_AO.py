import heapq

def a_estrella(grafo, inicio, objetivo, h):

    # Cola de prioridad: (f(n), nodo)
    frontera = []
    heapq.heappush(frontera, (h[inicio], inicio))

    # g(n): costo desde inicio hasta el nodo
    costo = {inicio: 0}

    visitados = set()

    while frontera:
        # Nodo con menor f(n)
        f_actual, nodo_actual = heapq.heappop(frontera)

        print(nodo_actual, end=" ")

        # Si llegamos al objetivo
        if nodo_actual == objetivo:
            return True

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, peso in grafo[nodo_actual]:

                # Calcular nuevo costo g(n)
                nuevo_costo = costo[nodo_actual] + peso

                # Si no existe o es mejor camino
                if vecino not in costo or nuevo_costo < costo[vecino]:
                    costo[vecino] = nuevo_costo

                    # f(n) = g(n) + h(n)
                    f = nuevo_costo + h[vecino]

                    heapq.heappush(frontera, (f, vecino))

    return False


# 🔹 Ejemplo
grafo = {
    'A': [('B',1), ('C',4)],
    'B': [('D',2), ('E',5)],
    'C': [('F',1)],
    'D': [],
    'E': [],
    'F': []
}

h = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 2,
    'F': 0
}

a_estrella(grafo, 'A', 'F', h)