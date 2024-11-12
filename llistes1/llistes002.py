quantes = int(input("Quantes paraules entraràs ? "))

paraules = []
for a in range(quantes):
    p = input("Entra una paraula -> ")
    paraules.append(p)

busca = input("Quina paraula vols trobar ? ")
q = 0
for e in paraules:
    if busca == e:
        q = q + 1

print(f"{busca} apareix {q} vegades")
