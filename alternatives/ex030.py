# 30 Fes un programa que donada una data, digui a quina estació de l'any correspon:
# Període 	Estació
# 21/03 – 20/06 	Primavera
# 21/06 – 20/09 	Estiu
# 21/09 – 20/12 	Tardor
# 21/12 – 20/03 	Hivern
##
dies_maxim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# dia = int(input("Entra el dia -> "))
# mes = int(input("Entra el mes -> "))
diames = input("Entra la data dd/mm -> ")
dia = int(diames.split("/")[0])
mes = int(diames.split("/")[1])

if dia > dies_maxim[mes - 1] or dia < 1 or mes < 1 or mes > 12:
    print("error en la data")
elif mes == 1 or mes == 2 :
    print("Hivern")
elif mes == 3:
    if dia <= 20:
        print("Hivern")
    else:
        print("Primavera")
elif mes== 4 or mes == 5:
    print("Primavera")
elif mes == 6:
    if dia <= 20:
        print("Primavera")
    else:
        print("Estiu")
elif mes == 6 or mes== 7 or mes == 8 or (mes == 9 and dia <= 20):
    print("Estiu")
else:
    print("Tardor")
