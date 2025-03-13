import sqlite3

class Funcions():

    def connecta(self, nom_fitxer):
        self.conn = sqlite3.connect(nom_fitxer)

    def desconnecta(self):
        self.conn.close()

    def demana_job_id():
        r = input("Entra el JOB_ID -> ")
        return r

    def demana_opcio(minim = 0, maxim = 4):
        print("1.- Mostra tots els JOBS")
        print("2.- Elimina un JOB")
        opcio = input(f"Entra una opcio ({minim}..{maxim})-> ")
        if opcio.isdigit():
            opcio = int(opcio)
        return opcio

    def select_jobs(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM JOBS")
        return c.fetchall()

    def delete_job(self, job_id):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM JOBS WHERE JOB_ID = ?", (job_id,))
        q = c.rowcount
        self.conn.commit()
        return  q

        
if __name__ == "__main__":
    print("Dins de funcions -> ", __name__)
