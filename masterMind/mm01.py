import random
DIGITS = 5

def genera_combinacio():
    combi = []
    q = 0
    while q < DIGITS:
        n = random.randint(1, 9)
        if not n in combi:
            combi.append(n)
            q = q + 1
    return combi

def demana_jugada():
    combinacio = int(input("Entra la teva jugada -> "))
    jugada = []
    while combinacio > 0:
        n = combinacio % 10
        combinacio = combinacio // 10
        jugada.append(n)
    ## És valid?
    jugada.reverse()
    return jugada

def jugada_valida(combinacio):
    if len(combinacio) != DIGITS:
        return False
    else:
        for i in range(len(combinacio) - 1):
            if combinacio[i] in combinacio[i+1:]:
                return False
    return True

def quants_hi_son(jugada, combinacio):
    q = 0
    for a in jugada:
        if a in combinacio:
            q = q + 1
    return q

def quants_hi_son_ben_posats(jugada, combinacio):
    q = 0
    for i in range(len(jugada)):
        if jugada[i] == combinacio[i]:
            q = q + 1
    return q

# Generem la combinació
combinacio = genera_combinacio()
print(combinacio)

while True:
    # Demanem la jugada al jugador
    jugada = demana_jugada()
    while not jugada_valida(jugada):
        jugada = demana_jugada()

    hi_son = quants_hi_son(jugada, combinacio)
    ben_posats = quants_hi_son_ben_posats(jugada, combinacio)
    print(f"N'hi ha {hi_son} i ben posats són {ben_posats}")
    if ben_posats == DIGITS:
        break;
