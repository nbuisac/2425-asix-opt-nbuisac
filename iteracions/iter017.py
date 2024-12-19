"""
17.-  Fes un programa que calculi el màxim comú divisor de dos números.
      El màxim comú divisor és el divisor de tots dos més gran que hi hagi.
      Si no trobem cap divisor, el 1 sempre ho serà. Podem fer-ho 
      provant números del menor d'ells a 1 com a molt o a 
      base de restes
"""
## Amb while
n1 = int(input("Entra un numero -> "))
n2 = int(input("Entra un numero -> "))
if n1 < n2:
    mcd = n1
else:
    mcd = n2
while n1 % mcd != 0 or n2 % mcd != 0:
    mcd = mcd - 1

print(f"mcd({n1}, {n2}) = {mcd}")
















## Amb for
n1 = int(input("Entra un numero -> "))
n2 = int(input("Entra un numero -> "))
if n1 < n2:
    numero_petit = n1
else:
    numero_petit = n2
for mcd in range(numero_petit, 0, -1):
    if n1 % mcd == 0 and n2 % mcd == 0:
        break

print(f"mcd({n1}, {n2}) = {mcd}")