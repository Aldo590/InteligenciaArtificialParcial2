def dls(grafo, nodo, objetivo, limite, visitados=None):

    # Si es la primera llamada, crear conjunto de visitados
    if visitados is None:
        visitados = set()

    # Si encontramos el objetivo, terminar
    if nodo == objetivo:
        return True

    # Si ya no podemos bajar más (límite alcanzado), detener
    if limite == 0:
        return False

    # Marcar nodo como visitado
    visitados.add(nodo)

    # Recorrer vecinos
    for vecino in grafo[nodo]:

        # Solo ir si no ha sido visitado
        if vecino not in visitados:

            # Llamada recursiva con menor profundidad disponible
            if dls(grafo, vecino, objetivo, limite - 1, visitados):
                return True  # Si lo encuentra, terminar todo

    return False  # Si no encontró en este camino


def iddfs(grafo, inicio, objetivo, max_profundidad):

    # Probar con diferentes límites de profundidad
    for limite in range(max_profundidad + 1):

        print(f"\nIntentando con límite = {limite}")

        # Ejecutar DLS con ese límite
        if dls(grafo, inicio, objetivo, limite):
            print("Encontrado!")
            return True

    # Si no lo encuentra en ningún límite
    print("No encontrado")
    return False


# 🔹 Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# 🔹 Ejecutar algoritmo
iddfs(grafo, 'A', 'F', 3)