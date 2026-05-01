import random

gamma = 0.9   # importancia del futuro
alpha = 0.1   # tasa de aprendizaje
epsilon = 0.2 # probabilidad de explorar

# Estados
estados = ['A', 'B', 'C']

# Acciones
acciones = {
    'A': ['ir_B', 'ir_C'],
    'B': ['ir_C'],
    'C': []
}

# Transiciones simuladas
transiciones = {
    ('A', 'ir_B'): ('B', 5),
    ('A', 'ir_C'): ('C', 10),
    ('B', 'ir_C'): ('C', 2)
}

# Inicializar Q(s,a)
Q = {}
for s in estados:
    for a in acciones.get(s, []):
        Q[(s, a)] = 0


def elegir_accion(s):
    # Estrategia epsilon-greedy

    if random.random() < epsilon:
        # Explorar: elegir acción aleatoria
        return random.choice(acciones[s])
    else:
        # Explotar: elegir mejor acción conocida
        return max(acciones[s], key=lambda a: Q[(s, a)])


# Simulación de episodios
for _ in range(20):

    estado = 'A'  # estado inicial

    while estado != 'C':  # hasta estado terminal

        accion = elegir_accion(estado)

        # Obtener resultado
        siguiente_estado, recompensa = transiciones[(estado, accion)]

        # Fórmula Q-Learning:
        # Q(s,a) ← Q(s,a) + α [R + γ max Q(s',a') - Q(s,a)]
        
        if acciones.get(siguiente_estado):
            max_q = max(Q[(siguiente_estado, a)] for a in acciones[siguiente_estado])
        else:
            max_q = 0  # estado terminal

        Q[(estado, accion)] = Q[(estado, accion)] + alpha * (
            recompensa + gamma * max_q - Q[(estado, accion)]
        )

        # Avanzar al siguiente estado
        estado = siguiente_estado


# Mostrar valores aprendidos
print("Q-values:")
for k, v in Q.items():
    print(k, ":", v)