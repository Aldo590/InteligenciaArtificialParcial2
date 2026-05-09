# Filtro de Kalman simple en 1D

# Función principal
def kalman_filtro(mediciones):

    # Estado inicial
    x = 0

    # Incertidumbre inicial
    P = 1

    # Modelo de transición
    F = 1

    # Modelo de observación
    H = 1

    # Ruido del proceso
    Q = 0.01

    # Ruido de medición
    R = 0.1

    estimaciones = []

    for z in mediciones:

        # Predicción del estado
        x = F * x

        # Predicción de incertidumbre
        P = F * P * F + Q

        # Ganancia de Kalman
        K = P * H / (H * P * H + R)

        # Corrección usando medición
        x = x + K * (z - H * x)

        # Actualizar incertidumbre
        P = (1 - K * H) * P

        # Guardar estimación
        estimaciones.append(x)

    return estimaciones


# Mediciones con ruido
mediciones = [1, 2, 1.8, 2.2, 2.0]

# Ejecutar filtro
resultado = kalman_filtro(mediciones)

print("Estimaciones:")
print(resultado)