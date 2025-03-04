import random

def crea_combinacio():
    c = []
    while len(c) < 6:
        n = random.randint(1, 49)
        if not n in c:
            c.append(n)
    c.sort()
    return c

def escriu_combinacio(c, f):
    for a in c:
        f.write(f"{a:3}")
    f.write("\n")

f = open("combinacions.txt", "w")
for n in range(1000000):
    combinacio = crea_combinacio()
    escriu_combinacio(combinacio, f)
f.close()