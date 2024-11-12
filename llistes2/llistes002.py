quantes = int(input("Quantes paraules entraras ? "))

llista = []
for a in range(quantes):
    paraula = input("Entra una paraula -> ")
    llista.append(paraula)

busca = input("Quina paraula vols buscar ? ")

trobades = 0
## Cal fer un recorregut per la llista
for paraula in llista:
    if "a" in paraula:
        trobades = trobades + 1

print(f"La paraula {busca} apareix {trobades} vegades a la llista entrada")