quantes = int(input("Nombre de paraules -> "))

paraules = []
for i in range(quantes):
    p = input(f"Entra la paraula {i + 1}/{quantes} -> ")
    paraules.append(p)

for po in paraules:
    print(po, end=" ")
print()

canviar = input("Entra la paraula que vols modificar -> ")
nova_paraula = input("Entra la paraula per la que vols modificar -> ")

q = 0
for i in range(len(paraules)):
    if paraules[i] == canviar:
        q = q + 1
        paraules[i] = nova_paraula ## aquí modifiquem la paraula de la llista

if q == 0:
    print(f"La paraula {canviar} no és a la llista inicial")

for po in paraules:
    print(po, end=" ")
print()
    