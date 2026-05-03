# Calcula P(A | C)
def probabilidad_condicionada(datos, evento, condicion):

    contador_evento = 0        # cuenta cuántas veces ocurre A y C
    contador_condicion = 0     # cuenta cuántas veces ocurre C

    for d in datos:

        if condicion(d):       # verificar si cumple C
            contador_condicion += 1

            if evento(d):      # verificar si también cumple A
                contador_evento += 1

    # evitar división entre cero
    if contador_condicion == 0:
        return 0

    # fórmula: P(A|C)
    return contador_evento / contador_condicion


# Calcula P(A ∩ B | C)
def probabilidad_conjunta_condicionada(datos, eventoA, eventoB, condicion):

    contador = 0               # cuenta A y B y C
    contador_condicion = 0     # cuenta solo C

    for d in datos:

        if condicion(d):       # si cumple C
            contador_condicion += 1

            # verificar si cumple A y B al mismo tiempo
            if eventoA(d) and eventoB(d):
                contador += 1

    # evitar división entre cero
    if contador_condicion == 0:
        return 0

    # fórmula: P(A ∩ B | C)
    return contador / contador_condicion


# Verifica independencia condicional
def independencia_condicional(datos, A, B, C, tolerancia=1e-5):

    # calcular probabilidades necesarias
    P_A_B_C = probabilidad_conjunta_condicionada(datos, A, B, C)  # P(A ∩ B | C)
    P_A_C = probabilidad_condicionada(datos, A, C)               # P(A | C)
    P_B_C = probabilidad_condicionada(datos, B, C)               # P(B | C)

    # comparar si se cumple:
    # P(A ∩ B | C) ≈ P(A | C) * P(B | C)
    return abs(P_A_B_C - (P_A_C * P_B_C)) < tolerancia


# -------------------------
# Ejemplo de uso
# -------------------------

datos = [
    {'lluvia': True, 'paraguas': True, 'nubes': True},
    {'lluvia': True, 'paraguas': True, 'nubes': True},
    {'lluvia': False, 'paraguas': False, 'nubes': False},
    {'lluvia': False, 'paraguas': True, 'nubes': True},
]

# Definir eventos como funciones
A = lambda d: d['paraguas']   # evento A
B = lambda d: d['lluvia']     # evento B
C = lambda d: d['nubes']      # condición C

# Verificar independencia condicional
resultado = independencia_condicional(datos, A, B, C)

print("¿Independencia condicional?:", resultado)