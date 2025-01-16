# 2. Validacio d'una resposta
def es_resposta_valida(resposta):
    resposta = resposta.strip()
    if len(resposta) == 1 and resposta.lower() in "sn":
        return True
    return False

# 1. Validacio d'una nota
def es_nota_valida(nota, valor_minim = 0, valor_maxim = 10):
    if valor_minim <= nota <= valor_maxim:
        return True
    else:
        return False
    # return valor_minim <= nota <= valor_maxim

def demana_nota(valor_minim = 0, valor_maxim = 10):
    n = float(input(f"Entra una nota ({valor_minim}..{valor_maxim}) -> "))
    while not es_nota_valida(n, valor_minim, valor_maxim):
        n = float(input(f"Entra una nota ({valor_minim}..{valor_maxim}) -> "))
    return n

"""
# Exercici 1
n = float(input("Entra una nota -> "))
if es_nota_valida(n, 2, 4):
    print("Correcte")
else:
    print("No correcte")
"""

"""
# Exercici 2
r = input("Vols continuar ? ")
while not es_resposta_valida(r):
    r = input("Vols continuar ? ")
"""

"""
n = demana_nota(valor_minim = 1, valor_maxim = 100)
print("La nota és", n)
"""

def multiplica(a, b):
    m = 0
    for i in range(a):
        # print(f"({i + 1}) Sumo {b}")
        m = m + b
    return m

def divideix(a, b):
    d = 0
    while a >= b:
        d = d + 1
        a = a - b
    return d

def suma_1_N(n):
    s = 0
    i = 1
    while i <= n:
        s = s + i
        i = i + 1
    return s
    # return sum(list(range (1, n + 1)))

print(divideix(120, 11))
d = divideix(48, 5)
print(d)
print(suma_1_N(10))
