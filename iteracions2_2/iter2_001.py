"""
1. Escriu un programa que demani una frase i digui quantes lletres a hi ha.
"""
frase = input("Entra una frase -> ")
q = 0
for lletra in frase:
    if lletra in "aàAÀáÁäÄ":
        q += 1
print(f"Hi ha {q} lletres `a`")