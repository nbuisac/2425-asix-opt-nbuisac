"""
8. Fes un programa que demani 10 números per teclat 
i que els sumi i ens mostri el resultat
"""
VEGADES = 3
llista = []
for i in range(VEGADES):
    numero = float(input("Entra un numero -> "))
    llista.append(numero)

suma = 0
for i in llista:
    suma = suma + i
print("La suma és ", suma, llista)

print("La suma es", sum(llista))