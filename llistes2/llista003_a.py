quantes = int(input("Nombre de paraules -> "))

paraules = []
for i in range(quantes):
    p = input(f"Entra la paraula {i + 1}/{quantes} -> ")
    paraules.append(p)

for po in paraules:
    print(po, end=" ")
print()

canviar = input("Entra la paraula que vols modificar -> ")

if canviar in paraules:
    nova_paraula = input("Entra la paraula per la que vols modificar -> ")
    while canviar in paraules:
        posicio = paraules.index(canviar)
        paraules[posicio] = nova_paraula

    for po in paraules:
        print(po, end=" ")
    print()