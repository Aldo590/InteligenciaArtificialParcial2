import itertools

def es_valido(asignacion, grafo):
    for var in asignacion:
        for vecino in grafo[var]:
            if vecino in asignacion and asignacion[var] == asignacion[vecino]:
                return False
    return True


def resolver_arbol(variables, dominios, grafo, asignacion):
    # Resolver el resto con backtracking simple
    if len(asignacion) == len(variables):
        return asignacion

    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        asignacion[var] = valor

        if es_valido(asignacion, grafo):
            resultado = resolver_arbol(variables, dominios, grafo, asignacion)
            if resultado:
                return resultado

        del asignacion[var]

    return None


def cutset_conditioning(variables, dominios, grafo, cutset):

    # Generar combinaciones del cutset
    combinaciones = list(itertools.product(*[dominios[v] for v in cutset]))

    for valores in combinaciones:

        asignacion = dict(zip(cutset, valores))

        # Verificar que la asignación inicial sea válida
        if not es_valido(asignacion, grafo):
            continue

        # Resolver resto del problema
        resultado = resolver_arbol(variables, dominios, grafo, asignacion)

        if resultado:
            return resultado

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

# Elegimos A como cutset
cutset = ['A']

sol = cutset_conditioning(variables, dominios, grafo, cutset)

print("Solución:", sol)