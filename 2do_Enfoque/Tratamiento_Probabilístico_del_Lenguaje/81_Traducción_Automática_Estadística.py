import random


# Diccionario probabilístico
traducciones = {

    "hola": [
        ("hello", 0.8),
        ("hi", 0.2)
    ],

    "mundo": [
        ("world", 1.0)
    ],

    "gato": [
        ("cat", 0.7),
        ("kitty", 0.3)
    ]
}


# Elegir traducción según probabilidad
def seleccionar(opciones):

    r = random.random()

    acumulado = 0

    for palabra, prob in opciones:

        acumulado += prob

        if r < acumulado:
            return palabra


# Traducir oración
def traducir(oracion):

    resultado = []

    palabras = oracion.lower().split()

    for palabra in palabras:

        # Verificar si existe traducción
        if palabra in traducciones:

            traduccion = seleccionar(traducciones[palabra])

            resultado.append(traduccion)

        else:

            resultado.append("[desconocido]")

    return " ".join(resultado)


# Texto original
texto = "hola mundo gato"


# Traducir
resultado = traducir(texto)

print("Texto original:")
print(texto)

print("\nTraducción:")
print(resultado)