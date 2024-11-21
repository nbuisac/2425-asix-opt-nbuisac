llista1 = [1, 2, 3, 4, 5, 4, 3, 4, 5, 4, 3, 2, 1]
canviar = 3
per = 33

print(llista1)
while canviar in llista1:
    i = llista1.index(canviar)
    llista1[i] = per

print(llista1)