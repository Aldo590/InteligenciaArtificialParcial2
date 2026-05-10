import matplotlib.pyplot as plt


# Datos de dos clases
clase_A_x = [1, 2, 2]
clase_A_y = [1, 2, 0]

clase_B_x = [6, 7, 8]
clase_B_y = [6, 7, 5]


# Graficar clase A
plt.scatter(clase_A_x, clase_A_y, label="Clase A")

# Graficar clase B
plt.scatter(clase_B_x, clase_B_y, label="Clase B")


# Línea separadora
x_linea = [0, 10]
y_linea = [4, 4]

plt.plot(x_linea, y_linea)


# Etiquetas
plt.xlabel("X")
plt.ylabel("Y")

plt.title("Separabilidad Lineal")

plt.legend()

plt.show()