import random


# Gramática probabilística
gramatica = {

    "S": [
        ("NP VP", 1.0)
    ],

    "NP": [
        ("Juan", 0.5),
        ("Maria", 0.5)
    ],

    "VP": [
        ("corre", 0.5),
        ("come", 0.5)
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

    # Si no es variable, devolver palabra
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