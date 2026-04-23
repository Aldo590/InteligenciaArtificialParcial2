def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()  # Crear conjunto vacío la primera vez

    print(nodo, end=" ")  # Mostrar el nodo actual
    visitados.add(nodo)   # Marcar como visitado

    for vecino in grafo[nodo]:  # Recorrer vecinos, Si esta marcado no ejecuta el for y se regresa al nodo anterior
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)  # Llamada recursiva


# 🔹 Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# 🔹 Ejecutar DFS
dfs(grafo, 'A')