def cbj(variables, dominios, grafo, asignacion={}, conflictos={}):
    
    # Si todas están asignadas → solución
    if len(asignacion) == len(variables):
        return asignacion, conflictos

    # Elegir variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    conflictos[var] = set()

    for valor in dominios[var]:

        valido = True
        conflicto_local = set()

        # Verificar restricciones
        for vecino in grafo[var]:
            if vecino in asignacion and asignacion[vecino] == valor:
                valido = False
                conflicto_local.add(vecino)

        if valido:
            asignacion[var] = valor

            resultado, conflictos = cbj(variables, dominios, grafo, asignacion, conflictos)

            if resultado:
                return resultado, conflictos

            del asignacion[var]

        else:
            conflictos[var].update(conflicto_local)

    # Si falla, saltar atrás
    if conflictos[var]:
        return None, conflictos

    return None, conflictos


# EJEMPLO
variables = ['A', 'B', 'C']

dominios = {
    'A': ['Rojo', 'Verde'],
    'B': ['Rojo', 'Verde'],
    'C': ['Rojo', 'Verde']
}

grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

solucion, _ = cbj(variables, dominios, grafo)

print("Solución:", solucion)