# 20. Volem calcular el preu d'una entrada de cinema:
#     Sabem que una entrada estàndard val 5 €.
#     Si tens carnet jove et fan un 15% de descompte.
#     Els dimarts fan un 20%.
#     El cap de setmana no fan cap descompte a ningú.
#     Només et poden fer un descompte.
# Fes un programa que demani per cada opció si es compleix o no (resposta s/n) 
# i ens digui el preu que hem de pagar. (escull l'ordre de preguntes correcte)

PREU = 5
cap_de_setmana = input("És cap de setmana (s/N)? ")
if len(cap_de_setmana.strip()) > 0 and cap_de_setmana.strip().lower()[0] == "s":
    print("Cap de setmana")
    descompte = 0
else:
    dimarts= input("És dimarts (s/N)? ")
    if dimarts == "s":
        print("Dimarts")
        descompte = 0.20
    else:
        carnet_jove = input("Tens el carnet jove (S/n)? ")
        if carnet_jove.lower() == "s":
            descompte = 0.15
        else:
            descompte = 0
        
preu_final = PREU - (PREU * descompte)

print(f"{PREU} - {descompte * 100}% = {preu_final}")
