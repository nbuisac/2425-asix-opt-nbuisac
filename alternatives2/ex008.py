# 8.- Fes un programa que ens demani la operació que volem fer
# (+, -, * ó /), dos valors i mostri el resultat pertinent.
operacions = "+-*/";
print("Operacions bàsiques")
print("=" * len("Operacions bàsiques"))
print("+ Suma")
print("- Resta")
print("* Producte")
print("/ Divisió")

print("S Sortir")

opcio = input("Escull una opció +-*/ --> ")



operacio_ok = True
if opcio in operacions:
    numero1 = float(input("Entra el primer valor -> "))
    numero2 = float(input("Entra el segon valor -> "))
    if opcio == "+":
        resultat = numero1 + numero2
    elif opcio == "-":
        resultat = numero1 - numero2
    elif opcio == "*":
        resultat = numero1 * numero2
    elif opcio == "/":
        if numero2 != 0:
            resultat = numero1 / numero2
        else:
            operacio_ok = False
    if operacio_ok == True:
        print(f"{numero1} {opcio} {numero2} = {resultat}")
    else:
        print("No es pot dividir per zero")
else:
    print("opció incorrecta")

