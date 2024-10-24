print("Resolem una equació de 1r grau\n\tax + b = 0")
a = int(input("Quant val a -> "))
if a != 0:
    b = int(input("Quant val b -> "))
    x = -b / a
    print(f"{a}x + {b} = 0 té per solució x = {x}")
else:
    print("Si a és 0 no és una equació de 1r grau")
