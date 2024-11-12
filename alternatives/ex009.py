graus = int(input("Entra el nombre de graus -> "))

graus = graus % 360

quadrant = graus // 90 + 1

print(f"{quadrant} quadrant")

# if graus < 90:
#     print("1r quadrant")
# elif graus < 180:
#     print("2n quadrant")
# elif graus < 270:
#     print("3r quadrant")
# else:
#     print("4t Quadrant")
