def dls(grafo, nodo, objetivo, limite, visitados=None):
    if visitados is None:
        visitados = set()

    if nodo == objetivo:
        return True

    if limite == 0:
        return False

    visitados.add(nodo)

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            if dls(grafo, vecino, objetivo, limite - 1, visitados):
                return True

    return False


def iddfs(grafo, inicio, objetivo, max_profundidad):
    for limite in range(max_profundidad + 1):
        print(f"\nIntentando con límite = {limite}")
        if dls(grafo, inicio, objetivo, limite):
            print("\nEncontrado!")
            return True

    print("\nNo encontrado")
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

iddfs(grafo, 'A', 'F', max_profundidad=3)