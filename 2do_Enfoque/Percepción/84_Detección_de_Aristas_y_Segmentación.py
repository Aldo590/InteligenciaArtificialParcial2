from PIL import Image, ImageFilter


# Abrir imagen
imagen = Image.open("imagen.jpg")


# Detectar bordes
bordes = imagen.filter(ImageFilter.FIND_EDGES)


# Convertir a escala de grises
gris = bordes.convert("L")


# Segmentación simple por umbral
segmentada = gris.point(
    lambda p: 255 if p > 100 else 0
)


# Guardar resultados
bordes.save("bordes.jpg")

segmentada.save("segmentada.jpg")


print("Procesamiento completado")