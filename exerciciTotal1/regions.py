import sqlite3

f = open("paises.csv", "rt", encoding="utf8")
linia = f.readline()
linia = f.readline()
regions = []
while linia != "":
    regio = linia.split(",")[-1].strip()
    if regio not in regions:
        regions.append(regio)
    linia = f.readline()
print(regions)

conn = sqlite3.connect("C:/Users/nbuisac/Downloads/empresa.db")
cur = conn.cursor()
sql = "SELECT IFNULL(MAX(REGION_ID), 0) FROM REGIONS"
cur.execute(sql)
dades = cur.fetchone()
region_id = dades[0] + 1
sql = "INSERT INTO REGIONS(REGION_ID, REGION_NAME) VALUES(?, ?)"
for region_name in regions:
    if region_name != "":
        print(f"fem INSERT de ({region_id}, {region_name})")
        cur.execute(sql, (region_id, region_name))
        region_id += 1
conn.commit()
conn.close()