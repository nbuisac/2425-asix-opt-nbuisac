import os
from funcions import Funcions

def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    f = Funcions()
    f.connecta(r"C:\Users\nbuisac\Downloads\empresa.db")
    cls()
    opcio = Funcions.demana_opcio()
    while opcio != 0:
        print("has escollit", opcio)
        if opcio == 1:
            files = f.select_jobs()
            for fila in files:
                print(fila)
        elif opcio == 2:
            job_id = Funcions.demana_job_id()
            eliminats = f.delete_job(job_id)
            print(f"{eliminats} registres eliminats")
        elif opcio == 3:
            pass
        elif opcio == 4:
            pass
        else:
            print("Opció incorrecta")
        input()
        cls()
        opcio = Funcions.demana_opcio()
    f.desconnecta()
    print("Adeu")


