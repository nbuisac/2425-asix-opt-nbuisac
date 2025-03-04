nom_fitxer = "dades.txt"
try:
    f = open(nom_fitxer, "rt", encoding="utf8")
    q = 0
    caracter = f.read(1)
    while caracter != '':
        if caracter != '\n':
            q = q + 1
        caracter = f.read(1)
    f.close()
    print(f"El fitxer {nom_fitxer} té {q} caràcters")

except FileNotFoundError:
    print("no trobo el fitxer", nom_fitxer)
except Exception as e:
    print("ERROR inesperat: ", e)