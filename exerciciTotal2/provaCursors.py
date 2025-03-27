import sqlite3

fitxer_db = r"C:\Users\nbuisac\Downloads\empresa.db"

conn = sqlite3.connect(fitxer_db)
sql1 = "SELECT department_id, department_name FROM departments"
cur1 = conn.cursor()
for fila in cur1.execute(sql1):
    print(f"{fila[0]} : {fila[1]}")
    cur2 = conn.cursor()
    sql2 = "SELECT LAST_NAME, FIRST_NAME, SALARY FROM EMPLOYEES WHERE DEPARTMENT_ID = ?"
    for empleat in cur2.execute(sql2, (fila[0], )):
        print(f"   {empleat[0]}, {empleat[1]} cobra {empleat[2]} ")

conn.close()