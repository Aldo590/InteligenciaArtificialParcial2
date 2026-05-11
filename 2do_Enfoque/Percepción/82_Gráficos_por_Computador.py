import matplotlib.pyplot as plt


# Coordenadas del cuadrado
x = [1, 1, 4, 4, 1]
y = [1, 4, 4, 1, 1]


# Dibujar figura
plt.plot(x, y)


# Configurar gráfica
plt.title("Gráficos por Computador")

plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.grid(True)

plt.axis("equal")


# Mostrar figura
plt.show()