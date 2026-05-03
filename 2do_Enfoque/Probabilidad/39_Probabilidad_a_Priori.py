# Función para calcular probabilidad a priori
def probabilidad_a_priori(datos, evento):

    ocurrencias = 0              # contador del evento
    total = len(datos)           # número total de datos

    # recorrer todos los datos
    for d in datos:

        if d == evento:          # si coincide con el evento
            ocurrencias += 1     # incrementar contador

    # evitar división entre cero
    if total == 0:
        return 0

    # calcular probabilidad
    P = ocurrencias / total

    return P


# Ejemplo de uso

datos = [
    'lluvia', 'sol', 'lluvia', 'nublado',
    'sol', 'lluvia', 'sol', 'sol'
]

# calcular P(lluvia)
resultado = probabilidad_a_priori(datos, 'lluvia')

print("P(lluvia) =", resultado)