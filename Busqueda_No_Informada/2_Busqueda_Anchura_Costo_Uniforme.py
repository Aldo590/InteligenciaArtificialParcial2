import heapq  # Cola de prioridad (min-heap)

def costo_uniforme(grafo, inicio, objetivo):
    # Cola de prioridad: (costo_acumulado, camino)
    cola = [(0, [inicio])]
    
    visitados = set()  # Evitar ciclos

    while cola:
        costo, camino = heapq.heappop(cola)  # Saca el camino mas barato
        nodo = camino[-1]  # Ultimo nodo del camino

        # Si llegamos al objetivo, regresar costo y camino
        if nodo == objetivo:
            return costo, camino

        if nodo not in visitados: # Si no lo hemos visitado, marcarlo como visitado
            visitados.add(nodo)

            # Explorar vecinos
            for vecino, peso in grafo[nodo]:    # Vecino y costo de la arista
                nuevo_camino = list(camino)     # Copiar camino actual
                nuevo_camino.append(vecino)     # Agregar vecino
                nuevo_costo = costo + peso      # Sumar costo

                # Meter a la cola con prioridad por costo
                heapq.heappush(cola, (nuevo_costo, nuevo_camino))

    return None  # Si no hay camino


# 🔹 Grafo con pesos (costo en cada arista)
grafo = {
    'A': [('B', 1), ('C', 5)],
    'B': [('F', 10)],
    'C': [('F', 1)],
    'F': []
}

# 🔹 Ejecutar algoritmo
resultado = costo_uniforme(grafo, 'A', 'F')

# 🔹 Mostrar resultado
print(resultado)  # (6, ['A', 'C', 'F'])