# Definir relaciones de la red
padres = {
    'X': ['A', 'B'],
    'C': ['X'],
    'D': ['X']
}

hijos = {
    'X': ['C', 'D'],
    'A': ['X'],
    'B': ['X'],
    'C': [],
    'D': []
}


def manto_de_markov(nodo):

    manto = set()

    # 1. Agregar padres de X
    if nodo in padres:
        for p in padres[nodo]:
            manto.add(p)

    # 2. Agregar hijos de X
    if nodo in hijos:
        for h in hijos[nodo]:
            manto.add(h)

            # 3. Agregar padres de los hijos
            if h in padres:
                for p in padres[h]:
                    manto.add(p)

    # 4. Eliminar el nodo mismo si aparece
    if nodo in manto:
        manto.remove(nodo)

    return manto


# Ejemplo

resultado = manto_de_markov('X')

print("Manto de Markov de X:", resultado)