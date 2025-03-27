import os
import sqlite3

def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

fitxer_db = r"C:\Users\nbuisac\Downloads\empresa.db"

opcions_MP = [
    "Llistar dades per pantalla",
    "Exportar dades en un fitxer",
    "Manteniment de Taules"
]

opcions_Taules = [
    "EMPLOYEES",
    "DEPARTMENTS",
    "JOBS",
    "LOCATIONS",
    "COUNTRIES",
    "REGIONS"
]

def menu(opcions):
    # cls()
    for i in range(len(opcions)):
        print(f"{i + 1}.- {opcions[i]}")
    print("\n0.-Sortir")

    opcio = input("Entra una opció -> ")
    while int(opcio) < 0 or int(opcio) > len(opcions):
        opcio = input("ERROR: Entra una opció -> ")
    return int(opcio)

def connecta():
    return sqlite3.connect(fitxer_db)

def mostra_Taula(taula):
    print(f"Dades de la taula {taula}")
    conn= connecta()
    cur = conn.cursor()
    sql = f"SELECT * FROM {taula}"
    for fila in cur.execute(sql):
        print("| " + " | ".join(str(f) for f in fila) + " |")
    conn.close()

def nova_REGION():
    try:
        region_id  = int(input("Entra el codi de Regió -> "))
        region_name  = input("Entra el nom de Regió -> ")
        sql = "INSERT INTO REGIONS(REGION_ID, REGION_NAME) VALUES(?, ?)"
        conn= connecta()
        try:
            cur = conn.cursor()
            cur.execute(sql, (region_id, region_name))
            conn.commit()
        except Exception as e: 
            print("ERROR1 en la transacció:", e)
        conn.close()
    except Exception as e: 
        print("ERROR2 en la transacció:", e)
                    
def nou_COUNTRY():
    country_id  = input("Entra el codi del Pais -> ").upper()
    country_name  = input("Entra el nom del Pais -> ")
    try:
        region_id  = int(input("Entra el codi de la Regió -> "))
        sql = "INSERT INTO COUNTRIES(country_id, country_name, region_id) VALUES(?, ?, ?)";
        conn = connecta()
        try:
            cur = conn.cursor()
            cur.execute(sql, (country_id, country_name, region_id))
            conn.commit()
        except Exception as e:
            print("ERROR en sentència -> ", e)
        conn.close()
    except Exception as e:
        print("ERROR -> ", e)


opcio = menu(opcions_MP)
while opcio != 0:
    if opcio == 1:
        opcio = menu(opcions_Taules)
        while opcio != 0:
            mostra_Taula(opcions_Taules[opcio - 1])
            opcio = menu(opcions_Taules)
    elif opcio == 2:
        pass
    elif opcio == 3:
        opcio = menu(["Nova REGION", "Nou COUNTRY"])
        while opcio != 0:
            if opcio == 1:
                nova_REGION()
            elif opcio == 2:
                nou_COUNTRY()
            opcio = menu(["Nova REGION", "Nou COUNTRY"])

    opcio = menu(opcions_MP)
