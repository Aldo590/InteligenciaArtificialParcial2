# Matriz de pagos del juego:
# (estrategia_A, estrategia_B) -> (pago_A, pago_B)
juego = {
    ('C', 'C'): (3, 3),  # ambos cooperan
    ('C', 'T'): (0, 5),  # A coopera, B traiciona
    ('T', 'C'): (5, 0),  # A traiciona, B coopera
    ('T', 'T'): (1, 1)   # ambos traicionan
}

# Estrategias posibles para ambos jugadores
estrategias = ['C', 'T']


def es_mejor_respuesta(jugador, estrategia, otra_estrategia):
    # jugador: 0 = A, 1 = B
    # estrategia: lo que está jugando este jugador
    # otra_estrategia: lo que juega el otro jugador

    mejor_valor = float('-inf')  # valor más alto encontrado

    # Probar todas las estrategias posibles
    for e in estrategias:

        # Construir el perfil dependiendo del jugador
        if jugador == 0:
            perfil = (e, otra_estrategia)  # A cambia, B fijo
        else:
            perfil = (otra_estrategia, e)  # B cambia, A fijo

        # Obtener el pago del jugador actual
        valor = juego[perfil][jugador]

        # Buscar el mejor valor posible
        if valor > mejor_valor:
            mejor_valor = valor

    # Construir el perfil con la estrategia actual
    if jugador == 0:
        perfil_actual = (estrategia, otra_estrategia)
    else:
        perfil_actual = (otra_estrategia, estrategia)

    # Verificar si esta estrategia da el mejor resultado posible
    return juego[perfil_actual][jugador] == mejor_valor


# Lista donde guardaremos los equilibrios encontrados
equilibrios = []

# Probar todas las combinaciones de estrategias (A, B)
for a in estrategias:
    for b in estrategias:

        # Verificar si ambos jugadores están jugando su mejor respuesta
        if es_mejor_respuesta(0, a, b) and es_mejor_respuesta(1, b, a):
            equilibrios.append((a, b))  # es equilibrio de Nash


# Mostrar resultados
print("Equilibrios de Nash:", equilibrios)