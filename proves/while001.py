siono = input("Vols continuar (s/n) ")
intents = 1
while siono != 's' and siono != 'n':
    if intents >= 3:
        break
    siono = input("Vols continuar (s/n) ")
    intents = intents + 1

print(f"Has dit {siono} amb {intents} intents")