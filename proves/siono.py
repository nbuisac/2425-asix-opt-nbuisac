## if !(siono == "s" or  siono == "n"):
##  if  siono != "s" and siono != "n":
siono = input("Vols continuar (s/N)")
while len(siono) != 1 or siono not in "sSnN":
    siono = input("Vols continuar (s/N)")
if siono in "sS":
    print("Has dit Sí")
else:
    print("Has dit No")
    

