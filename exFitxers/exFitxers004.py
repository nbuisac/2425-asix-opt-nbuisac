## A partir d'un fitxer amb les dades dels habitants d'uns municipis
#  on tenim, separat per un coixinet # els següents camps:
# Nom del municipi, total d'homes, total de dones, total d'habitants
# Exemple de dades
# -->                Agullana#448#461#909
# -->                Aiguaviva#403#399#802
# -->                Albanyà#85#83#168
# -->                Quart#2083#2016#4099
# 
# Feu un programa que ens:
#     demani un nom de municipi i tot seguit ens mostri:
# El recompte de municipis on hi ha més homes que dones
# El recompte de municipis on hi ha més dones que homes
# La suma total d'habitants homes
# La suma total d'habitants dones
# Les dades del municipi que hem demanat.
#
# Exemple d'execució
###       Entra el municipi -> quart
###       Municipis totals: 221
###               majoria homes en 146 municipis
###               majoria dones en 70 municipis
###       Habitants totals: 822952
###               homes 412397
###               dones 410555
###       Municipi: Quart  homes: 2083     dones: 2016     total: 4099



# import os
# os.system("cls")
nom_fitxer = "maresme.csv"
try:
    fl = open(nom_fitxer, encoding="utf8")
    municipi = input("Entra el municipi -> ")
    muni = municipi
    fila = fl.readline()
    qt = mh = md = ig = 0
    th = td = 0
    while fila != "":
        qt += 1
        dades = fila.split("#")
        homes = int(dades[1])
        dones = int(dades[2])
        total = int(dades[3])
        th += homes
        td += dones
        if homes > dones:
            mh += 1
        elif dones > homes:
            md += 1
        else:
            ig += 1
        if municipi.upper() == dades[0].upper():
            muni = dades
        fila = fl.readline()
    fl.close()
    print(f"Municipis totals: {qt}\n\tmajoria homes en {mh} municipis\n\tmajoria dones en {md} municipis")
    print(f"Habitants totals: {th + td}\n\thomes {th}\n\tdones {td}")
    if muni == municipi:
        print(f"Municipi: {muni} no trobat")
    else:
        print(f"Municipi: {muni[0]}\t homes: {muni[1]}\t dones: {muni[2]}\t total: {muni[3]}")
except Exception as e:
    print("Error -> ", e)
