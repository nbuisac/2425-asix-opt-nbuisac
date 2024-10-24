## Categoria d'edats

edat = int(input("Entra la teva edat -> "))

if edat >= 65:
    que_es = "Gran"

elif edat > 25:
    que_es = "Adult"
    
elif edat > 20:
    que_es = "Jove"
elif edat > 12:
    que_es = "Adolescent"
elif edat > 3:
    que_es = "Nen"
elif edat >= 0:
    que_es = "Infant"
else:
    que_es = "ERROR"

print(f"Ets {que_es}")