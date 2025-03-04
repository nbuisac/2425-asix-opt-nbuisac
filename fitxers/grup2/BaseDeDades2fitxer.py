import sqlite3
import csv

taula = input("Quina taula vols exportar ? -> ")

try:
    conn = sqlite3.connect(r"C:\Users\nbuisac\Downloads\empresa.db")
    c = conn.cursor()
    sql = "SELECT * FROM " + taula
    sql = input("Entra la consulta que vols fer -> ")
    c.execute(sql)
    c.description ## té el nom de les columnes
    f = open(taula + ".csv", "wt", newline="") ## Creem el fitxer de sortida
    expert_csv = csv.writer(f, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    expert_csv.writerow([a[0] for a in c.description])
    for fila in c:
        expert_csv.writerow(fila)
    f.close()
    conn.close()
except Exception as e:
    print("ERROR: ", e)