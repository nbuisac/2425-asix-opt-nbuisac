"""
3. Fes un programa que escrigui VEGADES vegades hola.
Fes-lo dues vegades, una amb for i l'altra amb while.
"""
VEGADES = 10
print("FOR")
for a in range(VEGADES):
    ## executa el codi VEGADES vegades
    print("Hola", end= " ")
print()

print("WHILE")
comptador = 0
while comptador < VEGADES:
    print("Hola", end= " ")
    comptador += 1
print()

print("WHILE True")
comptador = 0
while True:
    if comptador >= VEGADES:
        break
    print("Hola", end= " ")
    comptador += 1
print()

