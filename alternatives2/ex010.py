lletra = input("Entra una lletra -> ")
if lletra.islower():
    print("És minúscula")
elif lletra >= 'A' and lletra <= 'Z' or lletra in "ÀÈÌÒÙÁÉÍÓÚÄËÏÖÜÇÑ":
    print("És MASJÚSCULA")
else:
    print("No és lletra")
