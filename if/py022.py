## 22. Fes un programa que calculi la tarifa d'un pàrquing,
# sabent que val 1€ la hora o fracció, és a dir que 
# si hi estic 3 hores pago 3€, i 
# si hi estic 3 hores i cinc minuts pago 4€.
# Per simplificar, per entrar les dades demana separadament l'hora d'entrada,
# el minut d'entrada, hora de sortida i minut de sortida.
# Suposem que tarifiquem dintre del mateix dia.
PREU_HORA = 1.1

entrada = input("Entra l'hora d'entrada (hh:mm) -> ")
sortida = input("Entra l'hora de sortida (hh:mm) -> ")

hora_entrada = int(entrada.split(":")[0])
minut_entrada = int(entrada.split(":")[1])

print(f"Hora entrada -> {hora_entrada} Minut -> {minut_entrada}")

hora_sortida = int(sortida.split(":")[0])
minut_sortida = int(sortida.split(":")[1])

print(f"Hora sortida -> {hora_sortida} Minut -> {minut_sortida}")

if hora_entrada < 0 or hora_entrada > 23 or \
   hora_sortida < 0 or hora_sortida > 23 or \
   minut_entrada < 0 or minut_entrada > 59 or \
   minut_sortida < 0 or minut_sortida > 59:
   print("Error en l'entrada de dades (HH:MM)")
   exit(1)
elif hora_sortida < hora_entrada or \
   hora_entrada == hora_sortida and minut_entrada >= minut_sortida:
   print("ERROR: Has sortit abans d'entrar?")
   exit(2)
else:
    print("A veure quant has de pagar?")
    hores = hora_sortida - hora_entrada
    if minut_sortida > minut_entrada:
        hores = hores + 1

    preu = hores * PREU_HORA
    print(f"Has de pagar {preu} Euros per {hores} hores")
    exit(0)