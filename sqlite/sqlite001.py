# sqlite exercici001
import sqlite3

nom_db = "./empresa.db"

tasca = input("Entra el tipus de feina -> ").upper()
try:
    conn = sqlite3.connect(nom_db)
    c = conn.cursor()
    for fila in c.execute(f"SELECT * FROM JOBS WHERE job_id = ?", (tasca, )):
        print(fila)

    conn.close()
except Exception as e:
    print("Error", e)
