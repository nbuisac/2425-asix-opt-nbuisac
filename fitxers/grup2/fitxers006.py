# Exercici 6
# A partir d'un nom de fitxer ens diu quants caràcters té. Si el fitxer no existeix diu 0

nom_fitxer = input("Entra el nom del fitxer -> ")
try:
    f = open(nom_fitxer, "rt", encoding="utf8")
    q = 0
    caracter = f.read(1)
    while caracter != '':
        if q != '\n':
            q = q + 1
        caracter = f.read(1)

    f.close()
    print(f"El fitxer {nom_fitxer} té {q} caràcters")
except FileNotFoundError:
    print("Error: El fitxer no existeix")
except PermissionError:
    print("Error: Sense permisos")
except Exception as e:
    print("Error inesperat", e)

print("Finalitza el programa")
