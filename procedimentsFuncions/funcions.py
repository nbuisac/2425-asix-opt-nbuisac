def minim_maxim(*a):
    minim = a[0]
    maxim = a[0]
    for numero in a:
        if numero < minim:
            minim = numero
        else:
            if numero > maxim:
                maxim = numero
    return minim, maxim

def demana_nota():
    nota1 = float(input("Entra una nota (0, 10) -> "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("ERROR: Entra una nota (0, 10) -> "))
    return nota1

def mitjana(*n):
    suma = 0
    quants = 0
    for nota in n:
        suma = suma + nota
        quants = quants + 1
    return suma / quants

def escriu_mitjana(mitja):
    print(f"La mitjana és {mitja}")

