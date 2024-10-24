## 8. Fes un programa que ens demani la operació que volem fer (+, -, * ó /),
# dos valors i mostri el resultat pertinent.

print("Operacio entre dos valors")
print("1.- Suma")
print("2.- Resta")
print("3.- Producte")
print("4.- Divisió")
opcio = int(input("escull una copció -> "))

if opcio < 1 or opcio > 4:
    print("Opcio incorrecta")
else:
    numero1 = float(input("Entra el primer valor -> "))
    numero2 = float(input("Entra el segon  valor -> "))
    ok = True
    if opcio == 1:
        resultat = numero1 + numero2
    elif opcio == 2:
        resultat = numero1 - numero2
    elif opcio == 3:
        resultat = numero1 * numero2
    elif opcio == 4 and numero2 != 0:
        resultat = numero1 / numero2
    else:
        ok = False
        print("No es pot dividir per 0")
    if ok:
        print(f"{numero1} {"+-*/"[opcio - 1]} {numero2} = {resultat}")