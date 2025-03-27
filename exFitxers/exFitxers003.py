nom_fitxer = "emissionsCO2.csv"
## Codi INE
# Municipi
# Gasoil (tn)
# GLP (tn)
# Gas natural (tn)
# Electricitat (tn)
# Total (tn)
 
try:
    fl = open(nom_fitxer, encoding="utf8")
    municipi = input("Entra el municipi -> ")
    fila = fl.readline()
    fila = fl.readline()
    qt = q = 0
    while fila != "":
        qt += 1
        dades = fila.split("#")
        gasoil = float(dades[2])
        glp = float(dades[3])
        gasNatural = float(dades[4])
        electricitat = float(dades[5])
        total = float(dades[6])
        individual = (gasoil + glp + gasNatural + electricitat)
        if abs(individual - total) > 0.005:
            q = q + 1
            print(f"{dades[1]}:{individual} - {total}")
        if municipi.upper() == dades[1].upper():
            muni = fila
        fila = fl.readline()
    fl.close()
    print(f"Desquadren {q} municipis de {qt}")
    print(muni)
except Exception as e:
    print("Error -> ", e)
