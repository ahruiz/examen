#codigo para adivinar numero oculto
#generado aleatoriamente por el sistema
import random

print("*" * 90)
print("Codigo para adivinar numero escondido con 5 oportunidades para acertar....")

numEscon = random.randint(1, 100)
#numEscon = 33

for i in range(5):
    numUsr = int(input(f"Ingresa el numero: "))
    if numUsr == numEscon:
        print(f"¡¡¡ACERTASTE!!!.. en tu intento numero { i + 1}.....Felicidades")
        exit()
    else:
        print(f"¡¡¡FALLASTE!!!....te quedan {5 - (i + 1)} oportunidades")
