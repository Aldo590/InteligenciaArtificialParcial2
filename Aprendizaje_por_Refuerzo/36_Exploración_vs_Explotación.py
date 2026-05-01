import random

epsilon = 0.2  # 20% explorar, 80% explotar

# Ejemplo de valores Q ya aprendidos
Q = {
    ('A', 'ir_B'): 5,
    ('A', 'ir_C'): 10
}

acciones = ['ir_B', 'ir_C']


def elegir_accion():
    # Generar número aleatorio entre 0 y 1
    if random.random() < epsilon:
        # Exploración: elegir acción al azar
        accion = random.choice(acciones)
        print("Explorando:", accion)
    else:
        # Explotación: elegir la mejor acción conocida
        accion = max(acciones, key=lambda a: Q[('A', a)])
        print("Explotando:", accion)

    return accion


# Probar varias veces
for _ in range(10):
    elegir_accion()