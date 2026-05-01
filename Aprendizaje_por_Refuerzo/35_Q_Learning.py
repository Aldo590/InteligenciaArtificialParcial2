import random

gamma = 0.9    # importancia del futuro
alpha = 0.1    # qué tan rápido aprende
epsilon = 0.2  # probabilidad de explorar

# Estados
estados = ['A', 'B', 'C']

# Acciones disponibles
acciones = {
    'A': ['ir_B', 'ir_C'],
    'B': ['ir_C'],
    'C': []  # estado terminal
}

# Transiciones del entorno:
# (estado, acción) -> (siguiente_estado, recompensa)
transiciones = {
    ('A', 'ir_B'): ('B', 5),
    ('A', 'ir_C'): ('C', 10),
    ('B', 'ir_C'): ('C', 2)
}

# Inicializar Q(s,a) en 0
Q = {}
for s in estados:
    for a in acciones.get(s, []):
        Q[(s, a)] = 0


def elegir_accion(estado):
    # Estrategia epsilon-greedy

    if random.random() < epsilon:
        # Exploración: elegir acción aleatoria
        return random.choice(acciones[estado])
    else:
        # Explotación: elegir la mejor acción conocida
        return max(acciones[estado], key=lambda a: Q[(estado, a)])


# Entrenamiento (varios episodios)
for _ in range(20):

    estado = 'A'  # estado inicial

    # Ejecutar hasta llegar a estado terminal
    while estado != 'C':

        # Elegir acción
        accion = elegir_accion(estado)

        # Obtener resultado del entorno
        siguiente_estado, recompensa = transiciones[(estado, accion)]

        # Calcular el mejor valor futuro
        if acciones.get(siguiente_estado):
            max_q = max(Q[(siguiente_estado, a)] for a in acciones[siguiente_estado])
        else:
            max_q = 0  # estado terminal

        # Actualización de Q (fórmula principal)
        Q[(estado, accion)] = Q[(estado, accion)] + alpha * (
            recompensa + gamma * max_q - Q[(estado, accion)]
        )

        # Avanzar al siguiente estado
        estado = siguiente_estado


# Mostrar resultados
print("Valores Q aprendidos:")
for clave, valor in Q.items():
    print(clave, ":", valor)