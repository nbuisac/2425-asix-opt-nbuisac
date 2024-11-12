quantes = int(input("Entra el número de paraules -> "))

llista = []
for a in range(quantes):
    paraula = input("Entra una paraula -> ")
    llista.append(paraula)

print()

for e in llista:
    print(e, end=" ")