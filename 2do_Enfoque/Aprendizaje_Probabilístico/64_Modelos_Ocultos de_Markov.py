import random


# Estados ocultos
# True = lluvia
# False = no lluvia
estados = [True, False]


# Observaciones
# True = paraguas
# False = sin paraguas
observaciones = [True, False]


# Probabilidad inicial
P_inicial = {
    True: 0.5,
    False: 0.5
}


# Probabilidades de transición
# P(Xt | Xt-1)
P_transicion = {
    True: {
        True: 0.7,
        False: 0.3
    },

    False: {
        True: 0.3,
        False: 0.7
    }
}


# Probabilidades de observación
# P(E | X)
P_observacion = {
    True: {
        True: 0.9,
        False: 0.1
    },

    False: {
        True: 0.2,
        False: 0.8
    }
}


# Función para muestrear según probabilidades
def muestrear(distribucion):

    r = random.random()

    acumulado = 0

    for valor, prob in distribucion.items():

        acumulado += prob

        if r < acumulado:
            return valor


# Generar secuencia HMM
def modelo_markov_oculto(pasos):

    # Elegir estado inicial
    estado = muestrear(P_inicial)

    secuencia_estados = [estado]
    secuencia_obs = []

    for _ in range(pasos):

        # Generar observación según estado actual
        obs = muestrear(P_observacion[estado])

        secuencia_obs.append(obs)

        # Cambiar al siguiente estado
        estado = muestrear(P_transicion[estado])

        secuencia_estados.append(estado)

    return secuencia_estados, secuencia_obs


# Ejecutar modelo
estados_generados, observaciones_generadas = modelo_markov_oculto(5)

print("Estados ocultos:")
print(estados_generados)

print("Observaciones:")
print(observaciones_generadas)