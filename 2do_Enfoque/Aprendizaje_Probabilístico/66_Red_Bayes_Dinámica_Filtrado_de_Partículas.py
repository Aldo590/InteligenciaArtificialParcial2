import random


# Crear partículas iniciales
def inicializar_particulas(N):

    return [random.uniform(0, 10) for _ in range(N)]


# Simular movimiento del sistema
def mover(particula):

    # Movimiento con ruido
    return particula + random.uniform(-1, 1)


# Calcular peso según observación
def calcular_peso(particula, observacion):

    # Mientras más cerca de la observación,
    # mayor será el peso
    error = abs(particula - observacion)

    return 1 / (1 + error)


# Re-muestreo de partículas
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

    # Inicializar partículas
    particulas = inicializar_particulas(N)

    for obs in observaciones:

        # Propagar partículas
        particulas = [mover(p) for p in particulas]

        # Calcular pesos
        pesos = [calcular_peso(p, obs) for p in particulas]

        # Normalizar pesos
        total = sum(pesos)

        pesos = [w / total for w in pesos]

        # Re-muestrear
        particulas = remuestrear(particulas, pesos)

    return particulas


# Observaciones del sistema
observaciones = [5, 6, 5.5]

# Ejecutar filtro
resultado = filtro_particulas(observaciones)

print("Partículas finales:")
print(resultado[:10])