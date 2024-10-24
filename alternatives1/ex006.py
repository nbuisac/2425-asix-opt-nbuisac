## 6. Fes un programa que ens digui en quin ordre
# s'han introduït dos nombres pel teclat
# (creixent, decreixent o bé són iguals)
numero1 = float(input("Entra el primer numero -> "))
numero2 = float(input("Entra el segon numero  -> "))

if numero1 < numero2:
    print("Ordre Creixent")
elif numero1 > numero2:
    print("Ordre Decreixent")
else:
    print("Son iguals")