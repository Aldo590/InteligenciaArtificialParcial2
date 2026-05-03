def utilidad(llueve, llevo_paraguas):
    if llueve and not llevo_paraguas:
        return -50
    elif llueve and llevo_paraguas:
        return 20
    elif not llueve and llevo_paraguas:
        return -10
    else:
        return 30


def utilidad_esperada(llevo_paraguas, prob_lluvia):
    return (prob_lluvia * utilidad(True, llevo_paraguas) +
            (1 - prob_lluvia) * utilidad(False, llevo_paraguas))


# SIN información
p_lluvia = 0.4

EU_sin = max(
    utilidad_esperada(True, p_lluvia),
    utilidad_esperada(False, p_lluvia)
)


# CON información perfecta
# Sabes si llueve o no antes de decidir

# Si llueve (40%)
EU_lluvia = max(utilidad(True, True), utilidad(True, False))

# Si no llueve (60%)
EU_no_lluvia = max(utilidad(False, True), utilidad(False, False))

EU_con = 0.4 * EU_lluvia + 0.6 * EU_no_lluvia


# Valor de la información
VOI = EU_con - EU_sin

print("EU sin info:", EU_sin)
print("EU con info:", EU_con)
print("Valor de la información:", VOI)