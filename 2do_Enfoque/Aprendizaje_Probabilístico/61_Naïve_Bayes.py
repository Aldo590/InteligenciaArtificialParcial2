# Probabilidades a priori
P_spam = 0.4
P_no_spam = 0.6


# Probabilidades de palabras dado spam
P_oferta_dado_spam = 0.8
P_gratis_dado_spam = 0.7


# Probabilidades de palabras dado NO spam
P_oferta_dado_no_spam = 0.2
P_gratis_dado_no_spam = 0.1


# Clasificador Naive Bayes
def naive_bayes():

    # Probabilidad de spam usando independencia
    prob_spam = (
        P_spam *
        P_oferta_dado_spam *
        P_gratis_dado_spam
    )

    # Probabilidad de NO spam
    prob_no_spam = (
        P_no_spam *
        P_oferta_dado_no_spam *
        P_gratis_dado_no_spam
    )

    # Normalización
    total = prob_spam + prob_no_spam

    prob_spam /= total
    prob_no_spam /= total

    # Decisión final
    if prob_spam > prob_no_spam:
        return "SPAM", prob_spam
    else:
        return "NO SPAM", prob_no_spam


# Ejecutar clasificador
resultado, probabilidad = naive_bayes()

print("Clasificación:", resultado)
print("Probabilidad:", probabilidad)