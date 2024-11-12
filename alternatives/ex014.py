# 14 Fes un programa que digui si un any és de traspàs o no.
# Ho serà quan sigui múltiple de 4, com el 2020.
# Compte, els múltiples de 100 no són tots de traspàs,
# només aquells que són múltiples de 400 com el 2000 (1900 no va ser de traspàs).

any = int(input("Entra l'any -> "))
if (any % 400 == 0) or (any % 4 == 0 and any % 100 != 0):
    print("Traspàs")
else:
    print("No és de traspàs")