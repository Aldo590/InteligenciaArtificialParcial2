from PIL import Image


# Abrir imagen
imagen = Image.open("escritura.jpg")


# Convertir a escala de grises
gris = imagen.convert("L")


# Obtener tamaño
ancho, alto = gris.size


# Simular reconocimiento
# Supongamos que detectamos un número
numero_detectado = 5


# Mostrar información
print("Imagen procesada")

print("Tamaño:", ancho, "x", alto)

print("Número reconocido:", numero_detectado)