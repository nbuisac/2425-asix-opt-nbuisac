quantes_notes = 0
suma_notes = 0
nota = float(input("Entra una nota -> "))
while (nota < 0 or nota > 10) and nota != -1 :
    nota = float(input("ERROR: Entra una nota -> "))
while nota != -1:
    quantes_notes = quantes_notes + 1
    suma_notes = suma_notes + nota
    nota = float(input("Entra una nota -> "))
    while (nota < 0 or nota > 10) and nota != -1 :
        nota = float(input("ERROR: Entra una nota -> "))

mitjana = suma_notes / quantes_notes
print(f"La mitjana de les notes es {mitjana}")
