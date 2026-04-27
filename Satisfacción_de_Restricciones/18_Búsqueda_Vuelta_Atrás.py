def backtracking(nums, objetivo, camino, resultado):

    # Si la suma del camino es el objetivo
    if sum(camino) == objetivo:
        resultado.append(list(camino))
        return

    # Si nos pasamos, detener
    if sum(camino) > objetivo:
        return

    for num in nums:

        # Elegir
        camino.append(num)

        # Explorar
        backtracking(nums, objetivo, camino, resultado)

        # Deshacer (backtracking)
        camino.pop()


# 🔹 Ejemplo
nums = [1, 2, 3]
objetivo = 4
resultado = []

backtracking(nums, objetivo, [], resultado)
print("Soluciones:", resultado)