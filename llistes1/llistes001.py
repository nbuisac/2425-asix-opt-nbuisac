quantes = int(input("Quantes paraules entraràs ? "))

paraules = []
for a in range(quantes):
    p = input("Entra una paraula -> ")
    paraules.append(p)

for paraula in paraules:
    print(paraula, end=" ")

print("\nS'ha acabat")
