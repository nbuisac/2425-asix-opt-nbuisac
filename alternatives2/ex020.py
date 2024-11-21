# 20. Volem calcular el preu d'una entrada de cinema:
#     Sabem que una entrada estàndard val 5 €.
#     Si tens carnet jove et fan un 15% de descompte.
#     Els dimarts fan un 20%.
#     El cap de setmana no fan cap descompte a ningú.
#     Només et poden fer un descompte.
# Fes un programa que demani per cada opció si es compleix o no (resposta s/n) i 
# ens digui el preu que hem de pagar. (escull l'ordre de preguntes correcte)

## Cal organitzar bé les preguntes per no haver de preguntar si no cal.abs

## Primer preguntarem si és cap de setmana => 0%
## sino ho és cal saber si és diamrts => 20%
## si no és dimarts caldrà saber si tens carnet jove => 15%
## en cas contrari pagues l'entrada completa => 0%

PREU = 5
cap_de_setmana = input("És cap de setmana (s/N)? ")
if len(cap_de_setmana.strip()) > 0 and cap_de_setmana.strip()[0] in "Ss":
    print("Cap de setmana, no hi ha descompte")
    descompte = 0
else:
    dimarts = input("És dimarts (s/N)? ")
    if len(dimarts.strip()) > 0 and dimarts.strip()[0].upper() == "S":
        print("Descompte per ser dimarts")
        descompte = 0.20
    else:
        carnet_jove = input("Tens el carnet jove (S/n) ? ")
        if carnet_jove == "n" or carnet_jove == "N":
            print("No s'aplica cap descompte en dia laborable")
            descompte = 0
        else:
            print("Descompte per tenir Carnet jove")
            descompte = 0.15

preu_final = PREU - (PREU * descompte)

print(f"{PREU} - {descompte*100}% = {preu_final}")