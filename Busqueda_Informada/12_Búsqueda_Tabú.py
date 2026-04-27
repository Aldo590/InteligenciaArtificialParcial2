def busqueda_tabu(grafo, inicio, h, max_iter=10, tamaño_tabu=3):

    nodo_actual = inicio
    mejor = inicio

    lista_tabu = []  # Guarda nodos prohibidos temporalmente

    for _ in range(max_iter):

        vecinos = grafo[nodo_actual]

        # Filtrar vecinos que no estén en la lista tabú
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]

        # Si no hay vecinos válidos, terminar
        if not vecinos_validos:
            break

        # Elegir el mejor vecino (menor heurística)
        mejor_vecino = min(vecinos_validos, key=lambda x: h[x])

        nodo_actual = mejor_vecino  # Moverse

        # Actualizar mejor solución encontrada
        if h[nodo_actual] < h[mejor]:
            mejor = nodo_actual

        # Agregar a lista tabú
        lista_tabu.append(nodo_actual)

        # Mantener tamaño de la lista tabú
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)  # Elimina el más antiguo

        print("Actual:", nodo_actual, "Tabú:", lista_tabu)

    return mejor


# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

h = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 4,
    'E': 3,
    'F': 0
}

resultado = busqueda_tabu(grafo, 'A', h)
print("Mejor encontrado:", resultado)