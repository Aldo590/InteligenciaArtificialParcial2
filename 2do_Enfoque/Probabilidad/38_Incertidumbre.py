# Probabilidades iniciales
P_lluvia = 0.3

# Probabilidad de ver paraguas dado lluvia
P_paraguas_dado_lluvia = 0.9

# Probabilidad de ver paraguas sin lluvia
P_paraguas_dado_no_lluvia = 0.2

# Aplicar regla de Bayes:
# P(lluvia | paraguas)

numerador = P_paraguas_dado_lluvia * P_lluvia

denominador = (
    P_paraguas_dado_lluvia * P_lluvia +
    P_paraguas_dado_no_lluvia * (1 - P_lluvia)
)

P_lluvia_dado_paraguas = numerador / denominador

print("Probabilidad de lluvia dado paraguas:", P_lluvia_dado_paraguas)