## Nota de numèrica a Lletra
nota = float(input("Entra la nota numèrica -> "))
if nota < 0 or nota > 10:
    print("ERROR")
elif nota == 10:
    print("Matrícula")
elif nota >= 9:
    print("Excel·lent")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Apte")
else:
    print("No Apte")