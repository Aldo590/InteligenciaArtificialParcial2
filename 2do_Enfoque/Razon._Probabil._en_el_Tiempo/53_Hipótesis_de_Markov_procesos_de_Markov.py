import random

# Estados posibles
estados = ['Soleado', 'Lluvioso']

# Matriz de transición:
# P(siguiente | actual)
transiciones = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}


def siguiente_estado(actual):
    """
    Selecciona el siguiente estado según probabilidades
    """

    probs = transiciones[actual]

    r = random.random()  # número entre 0 y 1
    acumulado = 0

    for estado, prob in probs.items():
        acumulado += prob

        if r < acumulado:
            return estado


def proceso_markov(inicial, pasos):
    """
    Simula una cadena de Markov
    """

    estado = inicial
    secuencia = [estado]

    for _ in range(pasos):

        # obtener siguiente estado
        estado = siguiente_estado(estado)

        # guardar
        secuencia.append(estado)

    return secuencia


# Ejemplo

resultado = proceso_markov('Soleado', 10)

print("Secuencia:", resultado)