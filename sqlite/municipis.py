## Taula municipis
# CREATE TABLE municipis (
#     codiMunicipi INT PRIMARY KEY,
#     nomMunicipi VARCHAR(100),
#     codiProvincia INT);
import csv
import sqlite3
nom_fitxer = "Municipis_d_Espanya.csv"
f = open(nom_fitxer, "rt", encoding="utf8")
lector_csv = csv.DictReader(f)

conn = sqlite3.connect(r"C:\Users\nbuisac\Downloads\empresa.db")
cur = conn.cursor()
sql = """INSERT INTO municipis(codiMunicipi, nomMunicipi, codiProvincia)
VALUES(?, ?, ?)
"""

for linia in lector_csv:
    cur.execute(sql, (linia["Codi"], linia["Nom"], linia["Codi Província"]))
conn.commit()
conn.close()
f.close()
