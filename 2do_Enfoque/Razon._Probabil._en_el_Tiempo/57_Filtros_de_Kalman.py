def kalman_filtro(mediciones):

    # estado inicial (posición)
    x = 0

    # incertidumbre inicial
    P = 1

    # modelo (en este caso simple)
    F = 1   # no cambia mucho el estado
    H = 1   # observamos directamente

    # ruidos
    Q = 0.01   # ruido del proceso
    R = 0.1    # ruido de medición

    estimaciones = []

    for z in mediciones:


        # Predicción
  
        x = F * x
        P = F * P * F + Q


        # Actualización

        K = P * H / (H * P * H + R)   # ganancia de Kalman

        x = x + K * (z - H * x)       # corregir estado
        P = (1 - K * H) * P           # actualizar incertidumbre

        estimaciones.append(x)

    return estimaciones



# Ejemplo


mediciones = [1, 2, 1.8, 2.2, 2.0]

resultado = kalman_filtro(mediciones)

print("Estimaciones:", resultado)