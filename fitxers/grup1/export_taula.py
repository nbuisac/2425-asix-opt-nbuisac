import sqlite3
import csv

conn = sqlite3.connect(r"C:\Users\nbuisac\Downloads\empresa.db")
c = conn.cursor()
taula = input("Entra el fitxer a crear -> ")
sql = input("Entra la consulta sql -> ")
f = open(taula + ".csv", "w", newline='')
expert_csv = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
c.execute(sql)
expert_csv.writerow([a[0] for a in c.description])
expert_csv.writerows(c)
f.close()
conn.close()