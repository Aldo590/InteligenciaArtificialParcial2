from collections import Counter


# Corpus de texto
corpus = """
hola mundo
hola inteligencia artificial
hola python
python inteligencia artificial
"""


# Convertir texto en palabras
palabras = corpus.split()


# Contar frecuencia de palabras
frecuencias = Counter(palabras)


# Total de palabras
total = len(palabras)


# Calcular probabilidades
probabilidades = {}

for palabra, cantidad in frecuencias.items():

    probabilidades[palabra] = cantidad / total


# Mostrar resultados
print("Frecuencias:")

for palabra, cantidad in frecuencias.items():

    print(palabra, ":", cantidad)


print("\nProbabilidades:")

for palabra, prob in probabilidades.items():

    print(palabra, ":", round(prob, 3))