def forward_checking(asignacion, variables, dominios, grafo):

    # Si todas las variables están asignadas → solución
    if len(asignacion) == len(variables):
        return asignacion

    # Elegir una variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    # Probar cada valor del dominio
    for valor in dominios[var]:

        # Copiar dominios para poder restaurarlos después
        copia_dominios = {v: list(dominios[v]) for v in dominios}

        # Asignar valor
        asignacion[var] = valor

        valido = True

        # Forward Checking: revisar vecinos
        for vecino in grafo[var]:
            if vecino not in asignacion:

                # Eliminar valores incompatibles (mismo color)
                dominios[vecino] = [v for v in dominios[vecino] if v != valor]

                # Si un vecino se queda sin opciones → fallo
                if not dominios[vecino]:
                    valido = False
                    break

        # Si todo sigue válido, continuar
        if valido:
            resultado = forward_checking(asignacion, variables, dominios, grafo)
            if resultado:
                return resultado

        # Backtracking: deshacer cambios
        del asignacion[var]
        dominios.update(copia_dominios)

    return None


# EJEMPLO CON SOLUCIÓN

variables = ['A', 'B', 'C']

# 🔥 Ahora sí hay 3 colores
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

solucion = forward_checking({}, variables, dominios, grafo)

print("Solución encontrada:", solucion)