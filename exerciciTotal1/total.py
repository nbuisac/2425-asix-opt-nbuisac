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
    "Importar dades d'un fitxer",
    "Manteniment de Taules"
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

def carregaRegions():
    pass
    

def mostra_Taula(taula):
    print(f"Dades de la taula {taula}")
    conn= connecta()
    cur = conn.cursor()
    sql = f"SELECT * FROM {taula}"
    for fila in cur.execute(sql):
        print(" | ".join(str(f) for f in fila))
    conn.close()

def nova_REGION():
    ## Demanem les dades a l'usuari
    region_name = input("Entra el nom de la regió -> ")
    ## Esbrinem el codi de regió que li toca
    try:
        conn = connecta()
        cur = conn.cursor()
        sql = "SELECT IFNULL(MAX(REGION_ID), 0) FROM REGIONS"
        cur.execute(sql)
        valor = cur.fetchone()
        region_id = valor[0] + 1
        ## Afegim la regió a la BD
        sql = "INSERT INTO REGIONS(REGION_ID, REGION_NAME) VALUES(?, ?)"
        try:
            cur.execute(sql, (region_id, region_name))
            conn.commit()
        except Exception as e:
            print(e)
        conn.close()
        print(f"Regió creada amb codi {region_id}")
    except Exception as e:
        print(e)


def nou_COUNTRY():
    country_id = input("Entra el codi de pais -> ").upper()
    country_name = input("Entra el nom de pais -> ")
    try:
        region_id = int(input("Entra el codi de regió -> "))
        ## Ja tenim les dades, ja podem fer l'INSERT
        try:
            conn = connecta()
            cur = conn.cursor()
            sql = "INSERT INTO COUNTRIES(COUNTRY_ID, COUNTRY_NAME, REGION_ID) VALUES(?, ?, ?)"
            try:
                cur.execute(sql, (country_id, country_name, region_id))
                conn.commit()
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        conn.close()
    except Exception as e:
        print(e)

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
        opcio = menu(["Carrega regions", "Carrega paisos"])
        while opcio != 0:
            if opcio == 1:
                carregaRegions()
            elif opcio == 2:
                pass
            opcio = menu(["Carrega regions", "Carrega paisos"]) 
    elif opcio == 4:
        opcio = menu(["Nova REGION", "Nou COUNTRY"])
        while opcio != 0:
            ## Tractem les dades
            if opcio == 1:
                nova_REGION()
            elif opcio == 2:
                nou_COUNTRY()
            ## Preparem la següent opció
            opcio = menu(["Nova REGION", "Nou COUNTRY"])


    opcio = menu(opcions_MP)
