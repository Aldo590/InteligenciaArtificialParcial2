import random

def busqueda_online(grafo, inicio, objetivo):

    estado_actual = inicio
    visitados = set()

    while estado_actual != objetivo:

        print("Actual:", estado_actual)

        visitados.add(estado_actual)

        vecinos = grafo[estado_actual]

        # Filtrar vecinos no visitados
        vecinos_no_visitados = [v for v in vecinos if v not in visitados]

        # Si todos ya fueron visitados, elegir cualquiera
        if vecinos_no_visitados:
            siguiente = random.choice(vecinos_no_visitados)
        else:
            siguiente = random.choice(vecinos)

        # Moverse al siguiente estado
        estado_actual = siguiente

    print("Objetivo alcanzado:", estado_actual)
    return estado_actual


# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

busqueda_online(grafo, 'A', 'F')