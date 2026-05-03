import random

def contar_conflictos(var, valor, asignacion, grafo):
    conflictos = 0
    for vecino in grafo[var]:
        if asignacion.get(vecino) == valor:
            conflictos += 1
    return conflictos


def min_conflicts(variables, dominios, grafo, max_iter=100):

    # Asignación inicial aleatoria (completa)
    asignacion = {
        var: random.choice(dominios[var]) for var in variables
    }

    for _ in range(max_iter):

        # Encontrar variables en conflicto
        conflictos = [
            var for var in variables
            if contar_conflictos(var, asignacion[var], asignacion, grafo) > 0
        ]

        # Si no hay conflictos → solución
        if not conflictos:
            return asignacion

        # Elegir una variable en conflicto al azar
        var = random.choice(conflictos)

        # Elegir valor que minimiza conflictos
        mejor_valor = min(
            dominios[var],
            key=lambda val: contar_conflictos(var, val, asignacion, grafo)
        )

        # Asignar nuevo valor
        asignacion[var] = mejor_valor

        print("Asignación:", asignacion)

    return None


# EJEMPLO
variables = ['A', 'B', 'C']

dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde', 'Azul'],
    'C': ['Rojo', 'Verde', 'Azul']
}

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

sol = min_conflicts(variables, dominios, grafo)

print("Solución:", sol)