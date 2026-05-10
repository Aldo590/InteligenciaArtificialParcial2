import random


# Datos de entrada
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Salidas esperadas
y = [0, 0, 0, 1]


# Inicializar pesos
w1 = random.random()
w2 = random.random()

# Bias
b = random.random()

# Tasa de aprendizaje
lr = 0.1


# Función escalón
def activacion(x):

    if x >= 0:
        return 1
    else:
        return 0


# Entrenamiento
for epoch in range(20):

    for i in range(len(X)):

        x1, x2 = X[i]

        objetivo = y[i]

        # Suma ponderada
        suma = x1 * w1 + x2 * w2 + b

        # Salida de la neurona
        salida = activacion(suma)

        # Error
        error = objetivo - salida

        # Actualizar pesos
        w1 += lr * error * x1
        w2 += lr * error * x2

        # Actualizar bias
        b += lr * error


# Prueba
for entrada in X:

    x1, x2 = entrada

    suma = x1 * w1 + x2 * w2 + b

    salida = activacion(suma)

    print("Entrada:", entrada)
    print("Salida:", salida)