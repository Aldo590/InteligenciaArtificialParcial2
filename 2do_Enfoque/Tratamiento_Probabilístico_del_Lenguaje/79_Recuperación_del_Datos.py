# Base de datos simple
documentos = {

    1: "inteligencia artificial y aprendizaje",

    2: "redes neuronales profundas",

    3: "procesamiento de lenguaje natural",

    4: "aprendizaje supervisado y no supervisado"
}


# Función de búsqueda
def recuperar_datos(consulta):

    resultados = []

    # Recorrer documentos
    for id_doc, texto in documentos.items():

        # Verificar coincidencia
        if consulta.lower() in texto.lower():

            resultados.append((id_doc, texto))

    return resultados


# Consulta del usuario
consulta = "aprendizaje"


# Recuperar documentos
resultado = recuperar_datos(consulta)


# Mostrar resultados
print("Resultados encontrados:\n")

for id_doc, texto in resultado:

    print("Documento:", id_doc)

    print("Texto:", texto)

    print()