"""
2. Fes un programa que validi una resposta s/n. 
    Que demani una resposta s ó n, 
    i si no és s ó n que la torni a demanar, 
    i si no està ....
"""
siono = input("Vols continuar (s/n) ? ").strip().lower()
while siono != "s" and siono != "n":
    siono = input("Vols continuar (s/n) ? ").strip().lower()
print("Has dit", siono)