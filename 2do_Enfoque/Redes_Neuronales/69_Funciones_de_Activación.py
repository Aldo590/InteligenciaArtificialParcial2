import math


# Función escalón
def escalon(x):

    if x >= 0:
        return 1
    else:
        return 0


# Función sigmoide
def sigmoide(x):

    return 1 / (1 + math.exp(-x))


# Función tangente hiperbólica
def tanh(x):

    return math.tanh(x)


# Función ReLU
def relu(x):

    return max(0, x)


# Función Leaky ReLU
def leaky_relu(x):

    if x > 0:
        return x
    else:
        return 0.01 * x


# Valores de prueba
valores = [-2, -1, 0, 1, 2]


# Probar funciones
for v in valores:

    print("Valor:", v)

    print("Escalón:", escalon(v))

    print("Sigmoide:", sigmoide(v))

    print("Tanh:", tanh(v))

    print("ReLU:", relu(v))

    print("Leaky ReLU:", leaky_relu(v))

    print()