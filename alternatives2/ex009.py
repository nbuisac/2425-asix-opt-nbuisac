# 9.- Fes un programa que demani un angle en graus (0-360) i
# ens indiqui a quin quadrant es troba.
# Controla que l'angle que s'introdueixi sigui vàlid.
# Suposarem [0,90) és el 1rQ, [90,180) és el 2nQ, [180,270) és el 3rQ i [270,360) és el 4tQ.
# Pots fer l'exercici per qualsevol valor positiu (si és major que 360 també funcioni).

grausTotals = float(input("Entra els graus -> "))

# Posem els graus entre 0 i 360
graus = grausTotals % 360

# Posem els graus en valor positiu
if graus < 0:
    graus = 360 + graus;

if graus < 90:
    quadrant = "primer"
elif graus < 180:
    quadrant = "segon"
elif graus < 270:
    quadrant = "tercer"
else:
    quadrant = "quart"

print(f"{grausTotals} graus es troben al {quadrant} quadrant")

print(f"{grausTotals} graus es troben al {graus // 90 + 1} quadrant")