"""
10. Fes un programa que demani 2 números i calculi el producte a base de sumes.
Per exemple per calcular 5*3 ha de fer 5 + 5 + 5
"""
q = 0
negatius = 0
numero1 = float(input("Entra un numero -> "))
if numero1 < 0:
    numero1 = numero1 * -1
    negatius = negatius + 1
while numero1 != int(numero1):
    numero1 *= 10
    q = q + 1

numero2 = float(input("Entra un numero -> "))
if numero2 < 0:
    numero2 = numero2 * -1
    negatius = negatius + 1
while numero2 != int(numero2):
    numero2 *= 10
    q = q + 1

producte = 0
for a in range(int(numero1)):
    print("Sumo", numero2)
    producte += numero2

for a in range(q):
    producte = producte / 10
if negatius == 1:
    producte = producte * -1
print(f"{numero1} x {numero2} = {producte}")