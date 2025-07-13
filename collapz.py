#collatz
from colorama import Fore
import os

os.system("clear")

print(f"{Fore.YELLOW}pedimos un num al usuario y lo llevamos a collapsar a 1{Fore.WHITE}")
print("si es par: num // 2, si es impar: 3 * num + 1")
misNums = []

def collatz(number):
    while number != 1:
        if number % 2 == 0:
           
            num = number // 2
            misNums.append(num)

            number = num
            # if num == 1:
            #     break

        elif number % 2 == 1:
            num = (3 * number) + 1
            misNums.append(num)
            number = num 
            if num == 1:
                break
            
    print(misNums)        
    
try:       
    number = int(input(f"{Fore.YELLOW}Ingresa un numero: {Fore.WHITE}"))

    collatz(number)
    
except:
    print("Debes ingresar numeros enteros y no otro tipo de caracter....intenta de nuevo")    
