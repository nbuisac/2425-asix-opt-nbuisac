"""
1.- Escriu un programa que demani una frase i digui quantes lletres a hi ha.
"""
frase = input("Entra una frase -> ")
quantes = 0
for lletra in frase:
    if lletra in 'aàáäâAÀÁÄÂ':
        quantes += 1
print(f"hi ha {quantes} lletres `a`")