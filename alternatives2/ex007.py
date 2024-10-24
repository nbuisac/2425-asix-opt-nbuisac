# 7. Fes un programa que passi d'euros a pessetes i/o al revés.
# Ens ha de demanar quina operació volem fer i l'import pertinent.
# Cal aplicar el canvi que toqui (1€ = 166'386 ptes)
print("Canvi de Monedes")
print("1.- €uros a pessetes")
print("2.- Pessetes a €uros")
opcio = input("Entra una opció -> ")

if opcio == "1":
    euros = float(input("total d'€uros -> "))
    pessetes = int(round(euros * 166.386, 0))
    print(f"{euros:.2f} euros son {pessetes:n} pessetes")
elif opcio == "2":
    pessetes = int(input("total de pessetes -> "))
    euros = round(pessetes / 166.386, 2)
    print(f"{pessetes:n} pessetes son {euros:.2f} euros")
else:
    print("opció incorrecta")
