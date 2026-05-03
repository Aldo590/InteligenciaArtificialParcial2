gamma = 0.9   # factor de descuento
alpha = 0.1   # tasa de aprendizaje

# Estados
estados = ['A', 'B', 'C']

# Política fija (no cambia)
politica = {
    'A': 'ir_B',
    'B': 'ir_C',
    'C': None
}

# Transiciones simuladas (experiencia del agente)
# (estado, siguiente_estado, recompensa)
experiencias = [
    ('A', 'B', 5),
    ('B', 'C', 2),
    ('A', 'B', 5),
    ('B', 'C', 2)
]

# Inicializar valores
V = {s: 0 for s in estados}


# Aprendizaje TD(0)
for (s, s2, recompensa) in experiencias:

    # Fórmula TD:
    # V(s) ← V(s) + α [R + γ V(s') - V(s)]
    
    V[s] = V[s] + alpha * (
        recompensa + gamma * V[s2] - V[s]
    )


# Mostrar resultados
print("Valores aprendidos:", V)