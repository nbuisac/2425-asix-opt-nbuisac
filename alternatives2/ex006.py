## 6.- Fes un programa que ens digui en quin ordre s'han introduït
#      dos nombres pel teclat (creixent, decreixent o bé són iguals)

numero1 = int(input("Entra un numero -> "))
numero2 = int(input("Entra un altre numero -> "))

if numero1 > numero2:
    print("S'han entrat en ordre decreixent")
elif numero1 < numero2:
    print("S'han entrat en ordre creixent")
else:
    print("Són iguals")