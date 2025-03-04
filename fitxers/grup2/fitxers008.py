## 8 fitxers
## A partir d'un fitxer del tipus mostrat ens diu el nom de l'usuari major.
## (Si dos usuaris tenen la mateixa edat, només en mostra un).
nom_fitxer = "nomsedats.txt"

try:
    f = open(nom_fitxer, "r")
    edat_maxima = -1;
    nom_gran = ""
    nom = f.readline()
    while nom != "":
        ## tractem les dades havent llegit l'edat
        edat = int(f.readline())
        ## preparem la següent iteració
        nom = f.readline()
    f.close()
    print(f"El/la més gran és {nom_gran} i té {edat_maxima} anys")
except Exception as e:
    print("Error", e)
