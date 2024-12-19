### Programa que pensa un numero i l'usuari l'ha d'encertar
## fins que l'usuari l'encerta
## fins que l'usuari l'encerta o ha esgotat les possibilitats (3)
## fer que el programa pregunti si volem tornar jugar
import random
INTENTS = 3
comentaris=["Ohh", "Llàstima", "Quasi"]

while True:
    numero_maquina = random.randint(1, 10)
    for intent in range(INTENTS):
        numero = int(input("entra un numero -> "))
        if numero == numero_maquina:
            print(f"Molt bé, l'has encertat en {intent + 1} intents")
            break
        elif numero < numero_maquina:
            print("Més gran!!!")
        else:
            print("Més petit!!!")
    else:
        print(comentaris[random.randint(0, len(comentaris) - 1)], " El numero era", numero_maquina)
    continuar = input("Vols continuar (s/n) ? ")
    if continuar == "n" or continuar == "N":
        break
else:
    print("Fins una altra!")






