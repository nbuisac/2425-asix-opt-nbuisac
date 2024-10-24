print("Exercici 10.- Majúscula, minúscula !!!")
lletra = input("Entra una lletra -> ")
if len(lletra) != 1:
    print("He demanat una lletra!!!")
elif lletra.isupper():
    print(f"{lletra} és majúscula")
elif lletra.islower():
    print(f"{lletra} és minúscula")
else:
    print(f"{lletra} NO és lletra")