import random
import math


# Función sigmoide
def sigmoide(x):

    return 1 / (1 + math.exp(-x))


# Derivada de sigmoide
def derivada_sigmoide(x):

    return x * (1 - x)


# Datos de entrada
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Salidas esperadas
y = [0, 1, 1, 0]


# Pesos capa oculta
w1 = random.random()
w2 = random.random()

w3 = random.random()
w4 = random.random()

# Pesos capa salida
w5 = random.random()
w6 = random.random()

# Bias
b1 = random.random()
b2 = random.random()
b3 = random.random()

# Tasa de aprendizaje
lr = 0.5


# Entrenamiento
for epoch in range(10000):

    for i in range(len(X)):

        x1, x2 = X[i]

        objetivo = y[i]

        # Forward propagation

        # Neurona oculta 1
        h1 = sigmoide(x1 * w1 + x2 * w2 + b1)

        # Neurona oculta 2
        h2 = sigmoide(x1 * w3 + x2 * w4 + b2)

        # Neurona salida
        salida = sigmoide(h1 * w5 + h2 * w6 + b3)

        # Calcular error
        error = objetivo - salida

        # Backpropagation

        # Delta salida
        delta_salida = error * derivada_sigmoide(salida)

        # Delta capa oculta
        delta_h1 = delta_salida * w5 * derivada_sigmoide(h1)

        delta_h2 = delta_salida * w6 * derivada_sigmoide(h2)

        # Actualizar pesos salida
        w5 += lr * delta_salida * h1
        w6 += lr * delta_salida * h2

        # Actualizar bias salida
        b3 += lr * delta_salida

        # Actualizar pesos ocultos
        w1 += lr * delta_h1 * x1
        w2 += lr * delta_h1 * x2

        w3 += lr * delta_h2 * x1
        w4 += lr * delta_h2 * x2

        # Actualizar bias ocultos
        b1 += lr * delta_h1
        b2 += lr * delta_h2


# Probar red neuronal
for entrada in X:

    x1, x2 = entrada

    # Forward propagation
    h1 = sigmoide(x1 * w1 + x2 * w2 + b1)

    h2 = sigmoide(x1 * w3 + x2 * w4 + b2)

    salida = sigmoide(h1 * w5 + h2 * w6 + b3)

    print("Entrada:", entrada)

    print("Salida:", round(salida))