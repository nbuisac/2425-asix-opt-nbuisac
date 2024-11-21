# 4.- Escriu un programa que permeti crear una llista de paraules i que,
# a continuació, demani una paraula i 
# n'elimini de la llista la primera ocurrència.
# Al final mostra com ha quedat la llista.

paraules = []
q = int(input("Quantes paraules vols entrar ? "))
for i in range(q):
    paraula = input("Entra una paraula -> ")
    paraules.append(paraula)

print(paraules)
elimina = input("Quina paraula vols eliminar ? ")

if elimina in paraules:
    paraules.remove(elimina)
print(paraules)
