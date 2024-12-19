"""
8.- Fes un programa que demani 10 números per teclat
i que els sumi i ens mostri el resultat
"""
print("La suma és", sum([int(input("Entra un numero")) for a in range(3)]))

acumulador = 0
for i in range(10):
    numero = float(input("Entra un numero -> "))
    acumulador += numero

print("La suma total és", acumulador)

## versió amb llista
llista = []
for i in range(10):
    numero = float(input("Entra un numero -> "))
    llista.append(numero)

suma = sum(llista)

print("La suma total és", suma)

