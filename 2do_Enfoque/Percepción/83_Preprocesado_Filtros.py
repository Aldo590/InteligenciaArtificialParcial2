from PIL import Image, ImageFilter


# Abrir imagen
imagen = Image.open("imagen.jpg")


# Aplicar filtro de desenfoque
desenfoque = imagen.filter(ImageFilter.BLUR)

# Aplicar filtro de contorno
contorno = imagen.filter(ImageFilter.CONTOUR)

# Aplicar filtro de detalle
detalle = imagen.filter(ImageFilter.DETAIL)


# Guardar imágenes
desenfoque.save("desenfoque.jpg")

contorno.save("contorno.jpg")

detalle.save("detalle.jpg")


print("Filtros aplicados correctamente")