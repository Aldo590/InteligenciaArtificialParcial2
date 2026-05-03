from collections import deque

def es_consistente(x, y):
    # Restricción: valores deben ser diferentes
    return x != y


def ac3(variables, dominios, grafo):

    # Cola de arcos (pares de variables)
    cola = deque()

    for var in variables:
        for vecino in grafo[var]:
            cola.append((var, vecino))

    while cola:
        (x, y) = cola.popleft()

        if revisar(x, y, dominios):
            # Si dominio queda vacío → fallo
            if not dominios[x]:
                return False

            # Volver a revisar vecinos de x
            for vecino in grafo[x]:
                if vecino != y:
                    cola.append((vecino, x))

    return True


def revisar(x, y, dominios):
    cambiado = False

    for valor_x in dominios[x][:]:

        # Verificar si existe un valor compatible en Y
        if not any(es_consistente(valor_x, valor_y) for valor_y in dominios[y]):

            dominios[x].remove(valor_x)
            cambiado = True

    return cambiado


# EJEMPLO
variables = ['A', 'B', 'C']

dominios = {
    'A': ['Rojo', 'Verde'],
    'B': ['Rojo'],
    'C': ['Rojo', 'Verde']
}

grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

print("Antes:", dominios)

ac3(variables, dominios, grafo)

print("Después:", dominios)