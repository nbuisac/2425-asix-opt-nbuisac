nom_fitxer = "dades.txt"
notes = [0,0,0,0,0,0,0,0,0,0,0]
try:
    fl = open(nom_fitxer)
    q = 0
    sp = 0
    notaC = fl.readline()
    while notaC != "":
        q = q + 1
        notaF = float(notaC)
        notes[int(notaF // 1)] += 1
        if notaF < 5:
            print(notaF)
            sp = sp + 1
        notaC = fl.readline()
    fl.close()
    print(f"Hi ha {q} notes de les quals {sp} suspeses")
    for i in range(len(notes)):
        print(f"{i} -> {notes[i]}")
except Exception as e:
    print("Error -> ", e)
