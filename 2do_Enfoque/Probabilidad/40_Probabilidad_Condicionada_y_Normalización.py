def probabilidad_condicionada(datos, evento_A, condicion_B):
    """
    datos: lista de elementos (pueden ser tuplas o diccionarios)
    evento_A: función que define A
    condicion_B: función que define B
    """

    contador_AyB = 0  # ocurrencias de A y B
    contador_B = 0    # ocurrencias de B

    for d in datos:

        if condicion_B(d):       # cumple B
            contador_B += 1

            if evento_A(d):     # cumple A también
                contador_AyB += 1

    # evitar división entre cero
    if contador_B == 0:
        return 0

    return contador_AyB / contador_B


# Ejemplo

datos = [
    {'clima': 'lluvia', 'paraguas': True},
    {'clima': 'sol', 'paraguas': False},
    {'clima': 'lluvia', 'paraguas': True},
    {'clima': 'nublado', 'paraguas': True},
]

# A: lluvia
# B: paraguas
P = probabilidad_condicionada(
    datos,
    evento_A=lambda d: d['clima'] == 'lluvia',
    condicion_B=lambda d: d['paraguas'] == True
)

print("P(lluvia | paraguas) =", P)