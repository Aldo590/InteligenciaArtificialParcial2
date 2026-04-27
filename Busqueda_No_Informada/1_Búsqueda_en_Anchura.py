from collections import deque  # Importa una cola eficiente

def bfs_camino(grafo, inicio, objetivo):
    cola = deque([[inicio]])  # Cola con caminos (empezamos con [inicio])
    visitados = set()         # Conjunto para no repetir nodos

    while cola:  # Mientras haya caminos por explorar
        camino = cola.popleft()   # Saca el primer camino de la cola
        nodo = camino[-1]         # Toma el último nodo del camino

        if nodo == objetivo:      # Si llegamos al objetivo
            return camino         # Devolvemos el camino completo

        if nodo not in visitados: # Si no lo hemos visitado
            visitados.add(nodo)   # Lo marcamos como visitado

            for vecino in grafo[nodo]:  # Recorremos sus vecinos
                nuevo_camino = list(camino)  # Copiamos el camino actual
                nuevo_camino.append(vecino)  # Agregamos el vecino
                cola.append(nuevo_camino)    # Guardamos el nuevo camino en la cola

    return None  # Si no hay camino, devuelve None


# Definición del grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar búsqueda
resultado = bfs_camino(grafo, 'A', 'F')

# Mostrar resultado
print(resultado)  # ['A', 'C', 'F']