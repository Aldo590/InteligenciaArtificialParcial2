import re


# Texto de entrada
texto = """
Juan trabaja en OpenAI.
Maria vive en Guadalajara.
El correo es ejemplo@gmail.com
"""


# Extraer nombres propios
nombres = re.findall(r"\b[A-Z][a-z]+\b", texto)

# Extraer correos electrónicos
correos = re.findall(r"\S+@\S+", texto)


# Mostrar resultados
print("Nombres encontrados:")

for nombre in nombres:

    print(nombre)


print("\nCorreos encontrados:")

for correo in correos:

    print(correo)