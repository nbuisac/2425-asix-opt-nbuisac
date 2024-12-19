"""
28. Fes un programa que calculi el MCD per l'algorisme d'Euclides.
    Euclides diu que si un número és múltiple de l'altre, el petit és el MCD:
        De 24 i 6 el MCD és 6
    Euclides diu que si no són múltiple un de l'altre, 
        el MCD que hem de buscar és el del petit i el residu de la divisió entera entre tots dos:
            De 40 i 24 el MCD que hem de buscar és el de 24 i 16
"""
n1 = int(input("Entra un numero -> "))
n2 = int(input("Entra un numero -> "))
if n1 > n2:
    gran = n1
    petit = n2
else:
    gran = n2
    petit = n1
while gran % petit != 0:
    gran, petit = petit, gran % petit
print(f"mcd({n1}, {n2}) = {petit}")
