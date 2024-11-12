llista = list(range(1, 51, 7))

## Recorregut 1, no podem modificar el contingurt de la llista
for element in llista:
    print(element)

for i in range(len(llista)):
    print(i, "->", llista[i])