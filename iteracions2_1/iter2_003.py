"""
3.- Escriu un programa que vagi demanant números fins trobar el zero i
    digui quants valors s'han introduït.
"""
quants = 0
numero_que_tractem = float(input("Entra un numero -> "))
gran = numero_que_tractem
while numero_que_tractem != 0:
    ## Tracto les dades
    if numero_que_tractem > gran:
        gran = numero_que_tractem
    ## Preparo la següent interació
    numero_que_tractem = float(input("Entra un numero -> "))
print(f"El més gran és {gran}")