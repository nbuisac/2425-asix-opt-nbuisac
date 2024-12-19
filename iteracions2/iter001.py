# 1. Fes un programa que validi una nota (0..10) amb while.
# Que demani una nota, i si no està entre 0 i 10 que la torni a demanar,
# i si no està ....

nota = float(input("Entra una nota (0..10) ->"))
while nota < 0 or nota > 10:
    nota = float(input("Entra una nota (0..10) ->"))

print("La nota entrada és", nota)