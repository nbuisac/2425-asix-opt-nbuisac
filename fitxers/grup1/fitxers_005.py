nom_fitxer = "C:/Windows/System32/Drivers/etc/hosts"
try:
    f = open(nom_fitxer, "rt")
    print("Fitxer obert")
    linia = f.readline()
    q = 0
    while linia != '':
        # Tractem les dades
        q = q + 1
        ## preparem la següent interacio
        linia = f.readline()
    f.close()
    print(f"El fitxer {nom_fitxer} té {q} linies")

    f = open(nom_fitxer, "rt")
    print("Fitxer obert")
    linies = f.readlines()
    f.close()
    print(f"El fitxer {nom_fitxer} té {len(linies)} linies")
except FileNotFoundError:
    print("no trobo el fitxer", nom_fitxer)
except Exception as e:
    print("ERROR inesperat: ", e)