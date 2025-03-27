nom_fitxer = input("Entra el nom del fitxer a transformar -> ")
try:
    fl = open(nom_fitxer)
    try:
        fe = open(nom_fitxer + ".upper", "wt")
        c = fl.read(1)
        while c != "":
            fe.write(c.upper())
            c = fl.read(1)
        fe.close()
        print("Fitxer generat correctament -> ", nom_fitxer + ".upper")
    except Exception as e:
        print("Error -> ", e)
    fl.close()
except Exception as e:
    print("Error -> ", e)
