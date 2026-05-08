# Definición:
# El reconocimiento del habla convierte señales de voz en texto.

import random


# Palabras posibles reconocidas por el sistema
palabras = ["hola", "mundo", "python", "ia"]


# Probabilidades simuladas de reconocimiento
probabilidades = {
    "hola": 0.4,
    "mundo": 0.3,
    "python": 0.2,
    "ia": 0.1
}


# Función que simula el reconocimiento de una palabra
def reconocer_habla():

    # Número aleatorio entre 0 y 1
    r = random.random()

    acumulado = 0

    # Recorrer cada palabra y su probabilidad
    for palabra, prob in probabilidades.items():

        acumulado += prob

        # Seleccionar palabra según probabilidad
        if r < acumulado:
            return palabra


# Simular múltiples reconocimientos
def simulacion(repeticiones):

    resultados = []

    # Ejecutar varias veces el reconocimiento
    for _ in range(repeticiones):

        palabra = reconocer_habla()

        resultados.append(palabra)

    return resultados


# Ejecutar simulación
resultado = simulacion(10)

print("Palabras reconocidas:")
print(resultado)