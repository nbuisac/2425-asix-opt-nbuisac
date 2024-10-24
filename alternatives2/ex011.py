VOCALS = "aeiouAEIOUáéíóúÁÉÍÚÓàèìòùÀÈÌÒÙäëïöüÄËÏÖÜÂÊÎÔÛ"
lletra = input("Entra una lletra -> ")

if len(lletra) != 1:
    print("No és una lletra")
elif lletra[0] in VOCALS:
    print(f"{lletra[0]} SÍ és una vocal")
else:
    print(f"{lletra[0]} NO és una vocal")