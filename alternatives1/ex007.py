## 7. Fes un programa que passi d'euros a pessetes i/o al revés.
# Ens ha de demanar quina operació volem fer i l'import pertinent.
# Cal aplicar el canvi que toqui (1€ = 166'386 ptes)
CANVI = 166.386
print("Passem de ...")
print("1.- €uros a Pessetes")
print("2.- Pessetes a €uros")
opcio = input("Què vols fer ? ")

if opcio == "1":
    euros = float(input("Entra els €uros -> "))
    pessetes = round(euros * CANVI, 0)
    print(f"{euros:.2f} euros son {pessetes:n} pessetes")
elif opcio == "2":
    pessetes = int(input("Entra les pessetes -> "))
    euros = round(pessetes / CANVI, 2)
    print(f"{pessetes} pessetes son {euros:.2f} euros")
else:
    print("Opció incorrecta")



