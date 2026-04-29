def utilidad(llueve, llevo_paraguas):
    if llueve and not llevo_paraguas:
        return -50  # me mojo
    elif llueve and llevo_paraguas:
        return 20   # protegido
    elif not llueve and llevo_paraguas:
        return -10  # molestia
    else:
        return 30   # buen clima


def utilidad_esperada(llevo_paraguas, prob_lluvia):
    total = 0

    # Caso: llueve
    total += prob_lluvia * utilidad(True, llevo_paraguas)

    # Caso: no llueve
    total += (1 - prob_lluvia) * utilidad(False, llevo_paraguas)

    return total


# Probabilidad de lluvia
p_lluvia = 0.4

# Decisiones
EU_paraguas = utilidad_esperada(True, p_lluvia)
EU_no_paraguas = utilidad_esperada(False, p_lluvia)

print("EU llevar paraguas:", EU_paraguas)
print("EU no llevar:", EU_no_paraguas)

# Elegir mejor decisión
if EU_paraguas > EU_no_paraguas:
    print("Conviene llevar paraguas")
else:
    print("Conviene no llevar paraguas")