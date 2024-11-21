## 21. Fes un programa que donada una hora, minut i segon,
# incrementi un segon i mostri l'hora resultant.
# Cal verificar que l'hora estigui entre 0 i 23,
# els minuts entre 0 i 59 i els segons entre 0 i 59.

## Primer demanem les dades HH:MI:SS (junt o separat)
# hhmmss = input("Entra l'hora inicial (HH:MM:SS) -> ")
hh = int(input("Entra l'hora -> "))

if hh < 0 or hh > 23:
    print("Hora incorrecta")
else:
    mm = int(input("Entra els minuts -> "))
    if mm < 0 or mm > 59:
        print("Minuts incorrectes")
    else:
        ss = int(input("Entra els segons -> "))
        if ss < 0 or ss > 59:
            print("Segons incorrectes")
        else:
            ## Programa principal
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




## Calcularem un segon més


## Mostrarem la nova hora