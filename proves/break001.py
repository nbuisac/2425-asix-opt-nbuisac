quantes_notes = 0
suma_notes = 0
while True:
    nota = float(input("Entra una nota -> "))
    if nota == -1:
        break
    if nota < 0:
        print("ERROR")
        continue
    if nota > 10:
        print("ERROR")
        continue
    quantes_notes = quantes_notes + 1
    suma_notes = suma_notes + nota

mitjana = suma_notes / quantes_notes
print(f"La mitjana de les notes es {mitjana}")
