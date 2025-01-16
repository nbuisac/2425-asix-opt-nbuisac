## 1.- Fes una funció es_nota_valida que validi una nota
#      (valor admès de 0 a 10). Ha de retornar cert o fals.
def es_nota_valida(nota, nota_minima=0, nota_maxima=10):
    return nota >= nota_minima and nota <= nota_maxima

def es_resposta_valida(resposta):
    if len(resposta.strip()) == 1:
        if resposta.strip().lower() in 'sn':
            return True
    return False

def demana_nota(nota_minima = 0, nota_maxima = 10):
    nota = float(input("Entra una nota -> "))
    while not es_nota_valida(nota, nota_minima, nota_maxima):
        nota = float(input("Entra una nota -> "))
    return nota

def es_parell(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    # return numero % 2 == 0

n = demana_nota()
print("La nota és", n)
n = demana_nota(0, 20)
print("La nota és", n)
