def dls(grafo, nodo, objetivo, limite, visitados=None):
    # Inicializar conjunto de visitados solo la primera vez
    if visitados is None:
        visitados = set()

    print(nodo, end=" ")        # Mostrar el nodo actual
    visitados.add(nodo)         # Marcar como visitado

    # Si encontramos el objetivo
    if nodo == objetivo:
        return True

    # Si llegamos al límite de profundidad
    if limite == 0:
        return False

    # Explorar vecinos
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            encontrado = dls(grafo, vecino, objetivo, limite - 1, visitados) # Llamada recursiva con límite reducido
            if encontrado:
                return True

    return False


# 🔹 Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dls(grafo, 'A', 'F', limite=1)