def suma(*x):
    s = 0
    for numero in x:
        s = s + numero
    return s

print(suma())
print(suma(1, 2))
print(suma(3, 4, 5, 6))
print(suma(3, 4, 5, 6, 6, 4, 5, 6,34, 5, 45, 34, 435, 35))