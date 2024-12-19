"""
2. Escriu un programa que demani una frase i digui si hi ha alguna lletra a.
"""
VOCALS_A = 'aAáÁÀàäÄâÂ'
frase = input("Entra una frase -> ")
longitud = len(frase)
i = 0
trobat = False
while i < longitud and not trobat:
    print(f"Tracto {frase[i]}")
    j = 0
    while j < len(VOCALS_A) and not trobat:
        if VOCALS_A[j] == frase[i]:
            trobat = True
        j = j + 1
    i += 1
if trobat:
    print(f"hi ha la primera `a` a la posicio {i}")
else:
    print("No hi ha cap a")


































"""
trobat = False
for lletra in frase:
    print(f"Tracto {lletra}" )
    for a in "aàáäâAÀÁÄÂ":
        if a == lletra:
            trobat = True
            break
    if trobat:
        break            

if trobat == True:
    print("Sí hi ha alguna a")
"""

VOCALS_A = 'aAáÁÀàäÄâÂ'
frase = input("Entra una frase -> ")


trobat = False
for lletra in frase:
    if lletra in "aàáäâAÀÁÄÂ":
        trobat = True
        break




if trobat == True:
    print("Sí hi ha alguna a")
else:
    print("No hi ha cap a")
