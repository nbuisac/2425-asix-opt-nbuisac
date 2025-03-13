## Taula paisos
# CREATE TABLE paisos (
# 	codi CHAR(2) PRIMARY KEY,
# 	codi3 CHAR(3),
# 	nombre VARCHAR(100),
# 	name VARCHAR(100),
# 	prefixe INT
# );
import csv
import sqlite3

nom_fitxer = "paisos.csv"
f = open(nom_fitxer, "rt", encoding="utf8")
conn = sqlite3.connect(r"C:\Users\nbuisac\Downloads\empresa.db")
cur = conn.cursor()
sql = "insert into paisos(codi, codi3, nombre, name, prefixe) values (?, ?, ?, ?, ?)"
lector = csv.reader(f)
q = 0
for linia in lector:
    if q == 0:
        q = 1
    else:
        print(linia)
        cur.execute(sql, (linia[3], linia[4], linia[0], linia[1], linia[-1]))
conn.commit()
conn.close()

f.close()
