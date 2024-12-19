def demanaNota(minim, maxim):
    nota = float(input("Entra una nota (-1 per acabar): "))
    while (nota < minim or nota > maxim) and nota != -1:
        nota = float(input("ERROR: Torna a entrar una nota (-1 per acabar): "))
    return nota



notes = []
nota = demanaNota(1, 10)
while nota != -1:
    notes.append(nota)
    nota = demanaNota(1, 10)


print(notes)