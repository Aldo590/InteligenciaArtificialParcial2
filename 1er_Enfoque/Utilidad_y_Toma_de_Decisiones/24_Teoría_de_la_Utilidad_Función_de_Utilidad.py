def utilidad(resultado):
    # Asignar utilidad a cada resultado
    valores = {
        'ganar_mucho': 100,
        'ganar_poco': 50,
        'perder': -20
    }
    return valores[resultado]


def utilidad_esperada(opcion):
    # opcion = [(resultado, probabilidad), ...]
    total = 0

    for resultado, prob in opcion:
        total += prob * utilidad(resultado)

    return total


# Opciones
opcion_A = [
    ('ganar_mucho', 0.3),
    ('perder', 0.7)
]

opcion_B = [
    ('ganar_poco', 0.9),
    ('perder', 0.1)
]

# Calcular utilidad esperada
UA = utilidad_esperada(opcion_A)
UB = utilidad_esperada(opcion_B)

print("Utilidad A:", UA)
print("Utilidad B:", UB)

# Elegir mejor opción
if UA > UB:
    print("Elegir A")
else:
    print("Elegir B")