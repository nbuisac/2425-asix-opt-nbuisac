# fitxers 7
# A partir d'un fitxer amb format /etc/password 
# ens mostra el nom dels usuaris amb el seu id.
nom_fitxer = input("Entra el nom del fitxer -> ")
try:
    f = open(nom_fitxer, "r", encoding="utf8")
    fs = open("sortida.txt", "w")

    linia = f.readline()
    while linia != "":
        ## tractem la linia
        linia = linia.replace("\n", "")
        camps = linia.split(":")
        fs.write(f"Usuari: {camps[0]} uid: {camps[2]}\n")
        linia = f.readline()

    fs.close()
    f.close()
except Exception as e:
    print("ERROR", e)