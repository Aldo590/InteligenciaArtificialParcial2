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


def muestreo_directo():
    muestra = {}

    # Nubes
    muestra['nubes'] = random.random() < P_nubes

    # Lluvia
    p_lluvia = P_lluvia_dado_nubes[muestra['nubes']]
    muestra['lluvia'] = random.random() < p_lluvia

    # Paraguas
    p_paraguas = P_paraguas_dado_lluvia[muestra['lluvia']]
    muestra['paraguas'] = random.random() < p_paraguas

    return muestra


# Generar una muestra
print(muestreo_directo())