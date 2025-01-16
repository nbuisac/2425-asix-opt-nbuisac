NOTA_MINIMA = 1
NOTA_MAXIMA = 20
def es_nota_valida(nota):
    # return nota >= 0 and nota <= 10
    if nota >= NOTA_MINIMA and nota <= NOTA_MAXIMA:
        return True
    else:
        return False

def demana_nota():
    nota1 = float(input(f"Entra una nota ({NOTA_MINIMA}, {NOTA_MAXIMA}) -> "))
    while not es_nota_valida(nota1):
        nota1 = float(input(f"ERROR: Entra una nota ({NOTA_MINIMA}, {NOTA_MAXIMA}) -> "))
    return nota1


n = float(input("Entra una nota -> "))
while not es_nota_valida(n):
    n = float(input("ERROR: Entra una nota -> "))