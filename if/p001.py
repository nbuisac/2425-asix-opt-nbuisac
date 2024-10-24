import os

os.system("cls")

nom = input("Entra el teu nom : ")
edat = int(input("Entra la teva edat: "))

print("Hola", nom, "tens", edat, "anys")

if edat >= 18:
    print("Ets major d'edat")
else:
    print("Encara no pots votar")
    anys_que_falten = 18 - edat
    print("Et falten",  anys_que_falten, "anys per votar")

print("Fins una altra vegada")