import sqlite3
conn = sqlite3.connect(r"C:\Users\nbuisac\Downloads\empresa.db")
cur = conn.cursor()
sql = "SELECT * FROM paisos"
files = cur.execute(sql)