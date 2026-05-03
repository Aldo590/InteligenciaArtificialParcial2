from collections import deque  # Importa cola doble para BFS

def bidireccional(grafo, inicio, objetivo):

    # Si inicio y objetivo son el mismo nodo, devuelve directamente
    if inicio == objetivo:
        return [inicio]

    # Cola para la búsqueda desde el inicio
    cola_inicio = deque([[inicio]])

    # Cola para la búsqueda desde el objetivo
    cola_objetivo = deque([[objetivo]])

    # Guarda nodo: camino desde el inicio hasta ese nodo
    visitados_inicio = {inicio: [inicio]}

    # Guarda nodo: camino desde el objetivo hasta ese nodo
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:

        # Expansión desde el inicio
        # Extrae el primer camino de la cola
        camino_inicio = cola_inicio.popleft()

        # Obtiene el último nodo del camino
        nodo_inicio = camino_inicio[-1]

        # Recorre los vecinos del nodo actual
        for vecino in grafo[nodo_inicio]:

            # Si el vecino no ha sido visitado desde el inicio
            if vecino not in visitados_inicio:

                # Crea un nuevo camino agregando el vecino
                nuevo_camino = camino_inicio + [vecino]

                # Guarda el camino en visitados
                visitados_inicio[vecino] = nuevo_camino

                # Agrega el nuevo camino a la cola
                cola_inicio.append(nuevo_camino)

                # Verifica si el nodo ya fue visitado desde el otro lado
                if vecino in visitados_objetivo:

                    # Une los caminos
                    return nuevo_camino + visitados_objetivo[vecino][::-1][1:]

        # Expansión desde el objetivo

        # Extrae el primer camino de la cola
        camino_obj = cola_objetivo.popleft()

        # Obtiene el último nodo del camino
        nodo_obj = camino_obj[-1]

        # Recorre los vecinos del nodo actual
        for vecino in grafo[nodo_obj]:

            # Si el vecino no ha sido visitado desde el objetivo
            if vecino not in visitados_objetivo:

                # Crea un nuevo camino agregando el vecino
                nuevo_camino = camino_obj + [vecino]

                # Guarda el camino en visitados
                visitados_objetivo[vecino] = nuevo_camino

                # Agrega el nuevo camino a la cola
                cola_objetivo.append(nuevo_camino)

                # Verifica si el nodo ya fue visitado desde el inicio
                if vecino in visitados_inicio:

                    # Une los caminos correctamente
                    return visitados_inicio[vecino] + nuevo_camino[::-1][1:]

    # Si no se encuentra conexión entre inicio y objetivo
    return None


# Ejemplo de uso
grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E']
}

print(bidireccional(grafo, 'A', 'F'))