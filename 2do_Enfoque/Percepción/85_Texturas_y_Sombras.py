from PIL import Image, ImageEnhance, ImageFilter


# Abrir imagen
imagen = Image.open("imagen.jpg")


# Mejorar contraste para resaltar textura
contraste = ImageEnhance.Contrast(imagen)

textura = contraste.enhance(2.0)


# Crear sombra usando desenfoque
sombra = textura.filter(ImageFilter.GaussianBlur(8))


# Guardar resultados
textura.save("textura.jpg")

sombra.save("sombra.jpg")


print("Texturas y sombras procesadas")