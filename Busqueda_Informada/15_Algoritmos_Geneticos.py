import random

# Función fitness: cuenta número de 1s
def fitness(individuo):
    return sum(individuo)

# Generar individuo aleatorio
def crear_individuo(n):
    return [random.randint(0,1) for _ in range(n)]

# Selección: elegir el mejor de dos (torneo)
def seleccion(poblacion):
    a = random.choice(poblacion)
    b = random.choice(poblacion)
    return a if fitness(a) > fitness(b) else b

# Cruce: combinar dos padres
def cruce(padre1, padre2):
    punto = random.randint(1, len(padre1)-1)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

# Mutación: cambiar un bit
def mutacion(individuo, prob=0.1):
    for i in range(len(individuo)):
        if random.random() < prob:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico(tam_poblacion=6, longitud=5, generaciones=10):

    # Crear población inicial
    poblacion = [crear_individuo(longitud) for _ in range(tam_poblacion)]

    for gen in range(generaciones):

        nueva_poblacion = []

        # Generar nueva población
        for _ in range(tam_poblacion):

            # Seleccionar padres
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)

            # Crear hijo
            hijo = cruce(padre1, padre2)

            # Mutar hijo
            hijo = mutacion(hijo)

            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        # Mostrar mejor de la generación
        mejor = max(poblacion, key=fitness)
        print(f"Gen {gen}: {mejor} Fitness={fitness(mejor)}")

    # Resultado final
    return max(poblacion, key=fitness)


# Ejecutar
resultado = algoritmo_genetico()
print("Mejor solución:", resultado)