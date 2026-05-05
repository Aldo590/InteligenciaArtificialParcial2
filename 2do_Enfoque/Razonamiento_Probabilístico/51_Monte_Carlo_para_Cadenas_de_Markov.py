import random

# Probabilidades del modelo


P_nubes = 0.5  # P(Nubes)

# P(Lluvia | Nubes)
P_lluvia_dado_nubes = {
    True: 0.8,
    False: 0.2
}

# P(Paraguas | Lluvia)
P_paraguas_dado_lluvia = {
    True: 0.9,
    False: 0.1
}


# Muestreo de Nubes

def muestrear_nubes(lluvia):
    """
    Calcula P(nubes | lluvia) y genera una muestra
    usando distribución proporcional:
    P(nubes) * P(lluvia | nubes)
    """

    probs = {}  # probabilidades no normalizadas

    # Evaluar ambas posibilidades de nubes
    for nubes in [True, False]:

        # P(nubes)
        P_N = P_nubes if nubes else (1 - P_nubes)

        # P(lluvia | nubes)
        if lluvia:
            P_L = P_lluvia_dado_nubes[nubes]
        else:
            P_L = 1 - P_lluvia_dado_nubes[nubes]

        # Probabilidad conjunta (sin normalizar)
        probs[nubes] = P_N * P_L

    # Normalización (para que sumen 1)
    total = sum(probs.values())
    probs[True] /= total
    probs[False] /= total

    # Muestreo según probabilidad
    return random.random() < probs[True]



# Muestreo de Lluvia

def muestrear_lluvia(nubes, paraguas=True):
    """
    Calcula P(lluvia | nubes, paraguas)
    """

    probs = {}

    for lluvia in [True, False]:

        # P(lluvia | nubes)
        if lluvia:
            P_L = P_lluvia_dado_nubes[nubes]
        else:
            P_L = 1 - P_lluvia_dado_nubes[nubes]

        # P(paraguas | lluvia)
        P_P = P_paraguas_dado_lluvia[lluvia]

        # Probabilidad conjunta (sin normalizar)
        probs[lluvia] = P_L * P_P

    # Normalización
    total = sum(probs.values())
    probs[True] /= total
    probs[False] /= total

    # Muestreo
    return random.random() < probs[True]


# Algoritmo MCMC

def mcmc(N):
    """
    Ejecuta Gibbs Sampling para aproximar:
    P(lluvia | paraguas=True)
    """

    # Estado inicial (aleatorio)
    estado = {
        'nubes': random.choice([True, False]),
        'lluvia': random.choice([True, False]),
        'paraguas': True  # evidencia fija
    }

    # Contador de resultados
    conteo = {True: 0, False: 0}

    for _ in range(N):

        # 1. Actualizar Nubes usando el estado actual de lluvia
        estado['nubes'] = muestrear_nubes(estado['lluvia'])

        # 2. Actualizar Lluvia usando nubes y evidencia
        estado['lluvia'] = muestrear_lluvia(estado['nubes'], True)

        # 3. Registrar el valor actual de lluvia
        conteo[estado['lluvia']] += 1

    # Normalización final

    total = sum(conteo.values())

    conteo[True] /= total
    conteo[False] /= total

    return conteo



# Ejecución


resultado = mcmc(1000)

print("P(lluvia | paraguas) ≈", resultado)