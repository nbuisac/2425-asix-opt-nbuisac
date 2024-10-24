VOCALS = "aeiouAEIOUàèìòùáéíóúÀÈÌÒÙÁÉÍÓÚÄEÏÖÜäëïöüÂÊÎÔÛâÊÎÔÛ"
print("Exercici 11.- Vocal !!!")
lletra = input("Entra una lletra -> ")
if lletra in VOCALS:
    print(f"{lletra} és una Vocal")
else:
    print(f"{lletra} NO és una Vocal")