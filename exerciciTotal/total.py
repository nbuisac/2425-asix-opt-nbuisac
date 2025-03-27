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
    "Exportar dades en un fitxer"
]

opcions_Taules = [
    "EMPLOYEES",
    "DEPARTMENTS",
    "JOBS"
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
        print(" | ".join(str(f) for f in fila))
    conn.close()
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
        pass
    opcio = menu(opcions_MP)
