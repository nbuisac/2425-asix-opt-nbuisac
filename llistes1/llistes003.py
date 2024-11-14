# 3 Escriu un programa que permeti crear una llista de paraules i que, 
# a continuació, demani dues paraules i 
# substitueixi la primera ocurrència de la paraula cercada per la segona.
# Al final mostra com ha quedat la llista.

quantes = int(input("Quantes paraules entraràs ? "))
paraules = []
for i in range(quantes):
    p = input("Entra una paraula -> ")
    paraules.append(p)

busca = input("Quina paraula vols canviar ? ")
nova = input("Quina paraula vols posar-hi ? ")

print(paraules)

for i in range(len(paraules)):
    if paraules[i] == busca:
        paraules[i] = nova

print(paraules)

