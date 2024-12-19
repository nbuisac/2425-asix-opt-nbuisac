"""
8.- Fes un programa que demani 10 números per teclat
i que els sumi i ens mostri el resultat
"""
acc = 0
for i in range(10):
    numero = input("entra un numero -> ")
    while not numero.isnumeric():
        numero = input("entra un numero -> ")
    acc = acc + int(numero)

print(acc)