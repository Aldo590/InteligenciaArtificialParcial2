import random

# Acciones posibles
acciones = ['A', 'B']

# Política: probabilidad de elegir cada acción
# Inicialmente igual
politica = {
    'A': 0.5,
    'B': 0.5
}

# Recompensas simuladas
def obtener_recompensa(accion):
    if accion == 'A':
        return random.choice([1, 0])  # variable
    else:
        return 0.7  # constante


# Aprendizaje
alpha = 0.1  # tasa de aprendizaje

for _ in range(50):

    # Elegir acción según probabilidades
    accion = random.choices(acciones, weights=[
        politica['A'], politica['B']
    ])[0]

    recompensa = obtener_recompensa(accion)

    # Ajustar política (refuerzo simple)
    if accion == 'A':
        politica['A'] += alpha * recompensa
        politica['B'] -= alpha * recompensa
    else:
        politica['B'] += alpha * recompensa
        politica['A'] -= alpha * recompensa

    # Normalizar probabilidades
    total = politica['A'] + politica['B']
    politica['A'] /= total
    politica['B'] /= total


print("Política aprendida:", politica)