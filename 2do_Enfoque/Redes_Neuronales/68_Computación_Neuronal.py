import math
import random


# Función de activación sigmoide
def sigmoide(x):

    return 1 / (1 + math.exp(-x))


# Clase neurona artificial
class Neurona:

    def __init__(self, entradas):

        # Inicializar pesos aleatorios
        self.pesos = [random.random() for _ in range(entradas)]

        # Inicializar bias
        self.bias = random.random()

    # Procesar entradas
    def activar(self, entradas):

        suma = 0

        # Multiplicar entradas por pesos
        for e, p in zip(entradas, self.pesos):

            suma += e * p

        # Agregar bias
        suma += self.bias

        # Aplicar función de activación
        return sigmoide(suma)


# Crear neurona con 2 entradas
neurona = Neurona(2)


# Datos de entrada
entrada = [1, 0]


# Obtener salida
salida = neurona.activar(entrada)

print("Entrada:", entrada)
print("Salida:", salida)