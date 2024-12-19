"""
2.- Escriu un programa que demani una frase i digui si hi ha alguna lletra a.
"""
VOCALS_A = "aàáâäãAÀÁÂÄÃ"
frase = input("Entra una frase -> ")

for lletra in frase:
    print("miro la lletra", lletra)
    if lletra in VOCALS_A:
        l_he_trobat = True
        break
else:
    l_he_trobat = False

if l_he_trobat:
    print("Hi ha alguna `a`")
else:
    print("No hi ha cap `a`")