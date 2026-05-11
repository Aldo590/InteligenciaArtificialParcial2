from PIL import Image


# Abrir imagen
imagen = Image.open("imagen.jpg")


# Obtener tamaño de imagen
ancho, alto = imagen.size


# Simular detección de objeto
# Coordenadas del objeto
x1 = 50
y1 = 50

x2 = 200
y2 = 200


# Recortar objeto detectado
objeto = imagen.crop((x1, y1, x2, y2))


# Guardar objeto detectado
objeto.save("objeto_detectado.jpg")


print("Objeto detectado")

print("Tamaño original:", ancho, "x", alto)

print("Área detectada:", (x1, y1, x2, y2))