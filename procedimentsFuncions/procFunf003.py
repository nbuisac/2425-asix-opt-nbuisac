from funcions import *

n1 = demana_nota()
n2 = demana_nota()
n3 = demana_nota()
m = mitjana(n1, n2, n3)
p, g = minim_maxim(n1, n2, n3)
print(f"La menor és {p} i la major és {g}")
escriu_mitjana(m)
