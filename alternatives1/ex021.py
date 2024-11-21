# 21. Fes un programa que donada una hora, minut i segon,
# incrementi un segon i mostri l'hora resultant.
# Cal verificar que l'hora estigui entre 0 i 23,
# els minuts entre 0 i 59 i
# els segons entre 0 i 59.

hhmmss = input("Entra l'hora actual completa (HH:MM:SS) - >")
hh = int(hhmmss.split(":")[0])
# hh = int(input("Entra la hora -> "))
mm = int(hhmmss.split(":")[1])
ss = int(hhmmss.split(":")[2])

if hh < 0 or hh > 23:
    print("Hora incorrecta")
elif mm < 0 or mm > 59:
    print("Minut incorrecte")
elif ss < 0 or ss > 59:
    print("Segon incorrecte")
else:
    print(f"{hh:02d}:{mm:02d}:{ss:02d}")
    
    ss = ss + 1
    if ss == 60:
        ss = 0
        mm = mm + 1
        if mm == 60:
            mm = 0
            hh = hh + 1
            if hh == 24:
                hh = 0

    print(f"{hh:02d}:{mm:02d}:{ss:02d}")

