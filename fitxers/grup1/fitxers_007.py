nom_fitxer = "passwd"
try:
    f = open(nom_fitxer, "rt")
    for linia in f:
        ## tractem les dades
        linia = linia.replace("\n", "")
        camps = linia.split(":")
        print(f"username: {camps[0]} amb id {camps[2]} amb una shell {camps[6]}")

    f.close()
except FileNotFoundError:
    print("no trobo el fitxer", nom_fitxer)
except Exception as e:
    print("ERROR inesperat: ", e)