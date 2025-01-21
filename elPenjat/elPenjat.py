import random
from getpass import getpass

def demana_paraula():
    paraula = getpass("Entra una paraula -> ").strip().lower()

    return paraula

def crea_paraula_usuari(n):
    return '_' * n

def es_lletra(lletra):
    if len(lletra) == 1 and \
        ("a" <= lletra <= "z" or lletra == "ç" or lletra == "ñ"):
        return True
    else:
        return False


def demana_una_lletra():
    lletra = input("Entra una lletra : ").strip().lower()
    while len(lletra) != 1 or not es_lletra(lletra):
        lletra = input("Entra una lletra : ").strip().lower()
    return lletra

def omple_encerts(paraula_usuari, paraula_a_encertar, l):
    paraula_final = paraula_usuari
    for i in range(len(paraula_a_encertar)):
        if paraula_a_encertar[i] == l:
            paraula_final = paraula_final[:i] + l + paraula_final[(i+1):]

    return paraula_final

lletres_entrades = ""
lletres_encertades = ""
lletres_fallades = ""
errors = 0


paraula_a_encertar = demana_paraula()
print(paraula_a_encertar)
paraula_usuari = crea_paraula_usuari(len(paraula_a_encertar))
print(paraula_usuari)
while paraula_a_encertar != paraula_usuari:
    l = demana_una_lletra()
    ## Portem el comptador
    lletres_entrades = lletres_entrades + l
    if l in paraula_a_encertar:
        lletres_encertades = lletres_encertades + l
        paraula_usuari = omple_encerts(paraula_usuari, paraula_a_encertar, l)
        pass
    else:
        errors = errors + 1
        lletres_fallades = lletres_fallades + l
    print(paraula_usuari, lletres_fallades, errors)