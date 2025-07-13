#juego piedra papael y tij
import os
from random import choice
from colorama import Fore

os.system("clear")*10

print(f"{Fore.YELLOW}Juguemos PIEDRA, PAPEL y TIJERAAAAA....{Fore.WHITE}")

mov = ["piedra", "papel", "tijera"]

usuario = -1

while usuario not in mov:
    usuario = input("Introduce un movimiento: ").lower()

ia = choice(mov)

print(f"Usuario: {usuario}")
print(f"IA: {ia}")    

if ia == usuario:
    print("Hemos empatado....😜")
    
if ia == "tijera" and usuario == "papel":
    print(f"Hemos perdido....❌")
    
if ia == "tijera" and usuario == "piedra":
    print("Hemos ganado....✅")
    
if ia == "papel" and usuario == "piedra":
    print("Hemos perdido....❌")
    
if ia == "papel" and usuario == "tijera":
    print("Hemos ganado....✅")
    
if ia == "piedra" and usuario == "papel":
    print("Hemos ganado....✅")
    
if ia == "piedra" and usuario == "tijera":
    print("Hemos perdido....❌")