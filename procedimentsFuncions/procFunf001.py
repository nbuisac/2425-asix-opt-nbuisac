def suma(x, y):
    z = x + y
    return z

def major(x, y):
    if x > y:
        return x
    else:
        return y

def saluda(nom = "Anonim", missatge="Hola"):
    print(f"{missatge} {nom}")

salutacions = ["Hola", "Adéu", "passa-t'ho bé"]
noms = ["Maria", "Pau", "Carla", "Clara", "David", "Joan", "Anna"]
for posicio, nom in enumerate(noms):
    saluda(nom, salutacions[posicio % len(salutacions)])

saluda(missatge="Adeu")