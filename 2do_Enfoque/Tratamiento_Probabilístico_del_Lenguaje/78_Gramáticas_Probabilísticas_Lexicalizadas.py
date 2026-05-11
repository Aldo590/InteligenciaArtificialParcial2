import random


# Gramática lexicalizada
gramatica = {

    "S": [
        ("NP VP", 1.0)
    ],

    "NP": [
        ("Juan", 0.5),
        ("Maria", 0.5)
    ],

    "VP": [
        ("come pizza", 0.6),
        ("corre rapido", 0.4)
    ]
}


# Seleccionar regla según probabilidad
def seleccionar(reglas):

    r = random.random()

    acumulado = 0

    for produccion, prob in reglas:

        acumulado += prob

        if r < acumulado:
            return produccion


# Generar oración
def generar(simbolo):

    # Si no existe en la gramática,
    # devolver directamente
    if simbolo not in gramatica:
        return simbolo

    # Elegir producción
    produccion = seleccionar(gramatica[simbolo])

    resultado = []

    # Expandir símbolos
    for s in produccion.split():

        resultado.append(generar(s))

    return " ".join(resultado)


# Generar oración final
oracion = generar("S")

print("Oración generada:")
print(oracion)