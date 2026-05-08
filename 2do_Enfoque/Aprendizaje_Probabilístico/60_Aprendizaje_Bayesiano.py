# Probabilidad a priori de que un correo sea spam
P_spam = 0.4

# Probabilidad de NO spam
P_no_spam = 0.6

# Probabilidad de encontrar la palabra "oferta"
# dado que es spam
P_oferta_dado_spam = 0.8

# Probabilidad de encontrar la palabra "oferta"
# dado que NO es spam
P_oferta_dado_no_spam = 0.2


# Función de aprendizaje bayesiano
def bayes():

    # Calcular probabilidad total de "oferta"
    P_oferta = (
        P_oferta_dado_spam * P_spam +
        P_oferta_dado_no_spam * P_no_spam
    )

    # Aplicar Regla de Bayes
    P_spam_dado_oferta = (
        P_oferta_dado_spam * P_spam
    ) / P_oferta

    return P_spam_dado_oferta


# Ejecutar algoritmo
resultado = bayes()

print("P(Spam | Oferta) =", resultado)