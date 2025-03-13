## Programa que demani notes fins -1
## Les anirem guardant en una llista per tractar-les més tard

def demana_nota():
    ok = False
    n = input("Entra una nota entre 1 i 10 -> ")
    while ok == False:
        try:
            nf = float(n)
            if (nf >= 1 and nf <= 10) or nf == -1:
                ok = True
            else:
                n = input("ERROR: Entra una nota entre 1 i 10 -> ")
        except Exception:
            n = input("ERROR: Entra una nota entre 1 i 10 -> ")
    return nf

notes = []
nota = demana_nota()
while nota != -1:
    notes.append(nota)
    nota = demana_nota()

print(notes)

## En mostrarem la major, la menor i la mitjana
if len(notes) >= 1:
    menor = notes[0]
    major = notes[0]
    suma = notes[0]
    quants = 1
    for nota in notes[1:]:
        quants = quants + 1
        suma = suma + nota
        if nota > major:
            major = nota
        elif nota < menor:
            menor = nota
    print("Nota mínima -> ", menor)
    print("Nota màxima -> ", major)
    print("Nota mitjana -> ", suma / quants)

    ## Quantes vegades les notes han anat a la baixa
if len(notes) >= 2:
    ## Primera versió
    q = 0
    nota_anterior = notes[0]
    for nota in notes[1:]:
        if nota < nota_anterior:
            q += 1
        nota_anterior = nota
    print(f"Hem baixat de nota {q} vegades")

    ## Segona versió
    q = 0
    for i in range(1,quants):
        if notes[i] < notes[i - 1]:
            q += 1
    print(f"Hem baixat de nota {q} vegades")


