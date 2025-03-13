import random
dades = [random.randint(1, 10) for a in range(10)]
# dades = []
# nota = int(input("Entra una nota -1 per acabar -> "))
# while nota != -1:
#     ## Tractem les dades
#     dades.append(nota)
#     ## preparem la següent interació 
#     nota = int(input("Entra una nota -1 per acabar -> "))

suma = 0
q = 0
if len(dades) > 0:
    maxim = dades[0]
    minim = dades[0]
    for nota in dades:
        if nota > maxim:
            maxim = nota
        elif nota < minim:
            minim = nota
        suma = suma + nota
        q = q + 1
    print(f"Tenim {q} notes que sumen {suma}, la mitjana és {suma / q}")
    print(f"Les notes van de {minim} a {maxim}")

    suma = sum(dades)
    q = len(dades)
    print(f"Tenim {q} notes que sumen {suma}, la mitjana és {suma / q}")

    maxima = max(dades)
    minima = min(dades)
    print(f"Les notes van de {minima} a {maxima}")




for a in dades:
    print(a)