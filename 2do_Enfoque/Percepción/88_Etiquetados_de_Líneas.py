from PIL import Image, ImageDraw


# Crear imagen vacía
imagen = Image.new("RGB", (400, 300), "white")


# Crear objeto para dibujar
dibujo = ImageDraw.Draw(imagen)


# Dibujar líneas
dibujo.line((50, 50, 350, 50), fill="black", width=3)

dibujo.line((50, 150, 350, 150), fill="black", width=3)

dibujo.line((50, 250, 350, 250), fill="black", width=3)


# Etiquetas de líneas
etiquetas = [
    ("Línea A", (60, 20)),
    ("Línea B", (60, 120)),
    ("Línea C", (60, 220))
]


# Dibujar etiquetas
for texto, posicion in etiquetas:

    dibujo.text(posicion, texto, fill="blue")


# Guardar imagen
imagen.save("lineas_etiquetadas.jpg")


print("Etiquetado completado")