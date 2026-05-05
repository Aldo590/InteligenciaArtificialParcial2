import random

# Probabilidades
P_nubes = 0.5

P_lluvia_dado_nubes = {
    True: 0.8,
    False: 0.2
}

P_paraguas_dado_lluvia = {
    True: 0.9,
    False: 0.1
}


def muestreo_ponderado(evidencia):
    muestra = {}
    peso = 1

    # Nubes (no es evidencia)
    muestra['nubes'] = random.random() < P_nubes

    # Lluvia (no es evidencia)
    p_lluvia = P_lluvia_dado_nubes[muestra['nubes']]
    muestra['lluvia'] = random.random() < p_lluvia

    # Paraguas (ES evidencia)
    muestra['paraguas'] = evidencia

    # actualizar peso usando P(paraguas | lluvia)
    peso *= P_paraguas_dado_lluvia[muestra['lluvia']]

    return muestra, peso


def ponderacion_verosimilitud(N, evidencia=True):

    pesos = {True: 0, False: 0}

    for _ in range(N):

        muestra, w = muestreo_ponderado(evidencia)

        # acumular peso según el valor de la variable de interés
        pesos[muestra['lluvia']] += w

    # normalización
    total = sum(pesos.values())

    for k in pesos:
        pesos[k] /= total

    return pesos

# Ejemplo

resultado = ponderacion_verosimilitud(1000, True)

print("P(lluvia | paraguas) ≈", resultado)