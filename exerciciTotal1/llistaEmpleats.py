import sqlite3

fitxer_db = r"C:\Users\nbuisac\Downloads\empresa.db"

conn = sqlite3.connect(fitxer_db)
cur1 = conn.cursor()
cur2 = conn.cursor()
sql1 = "SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM DEPARTMENTS ORDER BY 2"
sql2 = "SELECT last_name, first_name FROM EMPLOYEES WHERE DEPARTMENT_ID = ?"
cur1.execute(sql1)
for departament in cur1:
    print(departament[1])
    cur2.execute(sql2, (departament[0],))
    q = 0
    for empleat in cur2:
        q += 1
        print(f"\t{empleat[0]}, {empleat[1]}")
    print(f"{q} empleats")
conn.close()