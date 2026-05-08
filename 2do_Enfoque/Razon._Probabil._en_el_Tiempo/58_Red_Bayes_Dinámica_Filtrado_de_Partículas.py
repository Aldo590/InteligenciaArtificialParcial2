import random

# Inicializar partículas
def inicializar_particulas(N):

    # partículas aleatorias entre 0 y 10
    return [random.uniform(0, 10) for _ in range(N)]


# Movimiento del sistema
def mover(particula):

    # movimiento con pequeño ruido
    return particula + random.uniform(-1, 1)


# Peso según observación
def calcular_peso(particula, observacion):

    # mientras más cerca de la observación, mayor peso
    error = abs(particula - observacion)

    return 1 / (1 + error)


# Re-muestreo
def remuestrear(particulas, pesos):

    nuevas = []

    for _ in range(len(particulas)):

        r = random.random()
        acumulado = 0

        for p, w in zip(particulas, pesos):

            acumulado += w

            if r < acumulado:
                nuevas.append(p)
                break

    return nuevas

# Filtro de partículas
def filtro_particulas(observaciones, N=100):

    # crear partículas iniciales
    particulas = inicializar_particulas(N)

    for obs in observaciones:

        # Propagación
        particulas = [mover(p) for p in particulas]

        # Calcular pesos
        pesos = [calcular_peso(p, obs) for p in particulas]

        # normalizar pesos
        total = sum(pesos)
        pesos = [w / total for w in pesos]

        # Re-muestreo
        particulas = remuestrear(particulas, pesos)

    return particulas


# Ejemplo

observaciones = [5, 6, 5.5]

resultado = filtro_particulas(observaciones)

print("Partículas finales:")
print(resultado[:10])  # mostrar primeras 10