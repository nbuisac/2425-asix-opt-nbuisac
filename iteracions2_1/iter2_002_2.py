"""
2.- Escriu un programa que demani una frase i digui si hi ha alguna lletra a.
"""
VOCALS_A = "aàáâäãAÀÁÂÄÃ"
frase = input("Entra una frase -> ")

i = 0
l_he_trobat = False
while i < len(frase):
    j = 0
    while j < len(VOCALS_A):
        print("Comprovo", frase[i], VOCALS_A[j])
        if frase[i] == VOCALS_A[j]:
            l_he_trobat = True
            break
        j += 1
    else:
        i += 1
        continue
    break

if l_he_trobat:
    print("Hi ha alguna `a`")
else:
    print("No hi ha cap `a`")