import csv

provincia = int(input("Entra el codi de província a exportar -> "))
fitxerLectura = "Municipis_D_Espanya.csv"
fitxerEscriptura = "Provincia_" + str(provincia).rjust(2, '0') + ".csv"

print(f"Generant el fitxer {fitxerEscriptura} ...")

fl = open(fitxerLectura, "rt", encoding="utf8", newline="")
lector = csv.reader(fl, quoting = csv.QUOTE_STRINGS)
fe = open(fitxerEscriptura, "wt", encoding="utf8", newline="")
escriptor=csv.writer(fe,quoting = csv.QUOTE_STRINGS)
q = 0
for linia in lector:
    if q == 0:
        q = 1
        continue
    if int(linia[2]) == provincia:
        linia[0] = int(linia[0])
        linia[2] = int(linia[2])
        print(linia)
        escriptor.writerow(linia)


print("Feina feta :)")