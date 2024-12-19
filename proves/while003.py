## Encerta el numero
import random

MINIM = 1
MAXIM = 10

## generem el numero amb la màquina
for a in range(1000):
    numero_pensat = random.randint(MINIM, MAXIM)
    print(numero_pensat, end=" ")

print()



