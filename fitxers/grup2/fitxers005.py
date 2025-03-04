# Exercici 5
# A partir d'un nom de fitxer ens diu quantes línies té. Si el fitxer no existeix diu 0

nom_fitxer = input("Entra el nom del fitxer -> ")
try:
    f = open(nom_fitxer, "rt")
    q = 0
    linia = f.readline()
    while linia != "":
        q = q + 1
        linia = f.readline()
    f.close()
    print(f"El fitxer {nom_fitxer} té {q} linies")
    
    f = open(nom_fitxer, "rt")
    linies = f.readlines()
    q = len(linies)
    f.close()
    print(f"El fitxer {nom_fitxer} té {q} linies")
except FileNotFoundError:
    print("Error: El fitxer no existeix")
except PermissionError:
    print("Error: Sense permisos")
except Exception as e:
    print("Error inesperat", e)

print("Finalitza el programa")
