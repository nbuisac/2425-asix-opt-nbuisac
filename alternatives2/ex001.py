print("Resolem una equació de 1r grau\n\tax + b = 0 ")
a = float(input("Entra el valor de a -> "))
b = float(input("Entra el valor de b -> "))
if a == 0:
    print("No hi ha solució")
else:
    x = -b / a
    print(f"per l'equació {a}x + {b} = 0, la x={x}")



