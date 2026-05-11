from PIL import Image, ImageChops


# Abrir dos imágenes consecutivas
imagen1 = Image.open("frame1.jpg")

imagen2 = Image.open("frame2.jpg")


# Calcular diferencia entre imágenes
diferencia = ImageChops.difference(imagen1, imagen2)


# Guardar resultado
diferencia.save("movimiento.jpg")


print("Movimiento detectado")