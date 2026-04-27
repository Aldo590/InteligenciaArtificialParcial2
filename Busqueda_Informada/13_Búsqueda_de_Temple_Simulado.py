import random
import math

def temple_simulado(grafo, inicio, h, T_inicial=10, enfriamiento=0.9):

    nodo_actual = inicio
    mejor = inicio
    T = T_inicial  # Temperatura inicial

    while T > 0.1:  # Condición de parada

        vecinos = grafo[nodo_actual]

        # Si no hay vecinos, termina
        if not vecinos:
            break

        # Elegir vecino aleatorio
        vecino = random.choice(vecinos)

        # Diferencia de heurística
        delta = h[vecino] - h[nodo_actual]

        # Si mejora, aceptar siempre
        if delta < 0:
            nodo_actual = vecino

        else:
            # Aceptar con probabilidad
            prob = math.exp(-delta / T)
            if random.random() < prob:
                nodo_actual = vecino

        # Actualizar mejor solución
        if h[nodo_actual] < h[mejor]:
            mejor = nodo_actual

        # Enfriamiento
        T = T * enfriamiento

        print("Actual:", nodo_actual, "T:", round(T,2))

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

resultado = temple_simulado(grafo, 'A', h)
print("Mejor encontrado:", resultado)