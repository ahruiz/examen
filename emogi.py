import random
from colorama import Fore


# print("Lanzamiento de dado....")
# print(f"🎲:{random.randint(1,6)}")

# #*************************************************************

# usr = "admin"
# pasw = "123"

# print("Bienvenido al sistema")
# numInt = 0

# while numInt <= 3:
#     u_usr = input("\nUsuario: ").lower()
#     p_pasw = input("Contraseña: ").lower()
    
#     if (usr,pasw) == (u_usr,p_pasw):
#         break
    
#     print("ERROR: Los datos ingresados no se encuentran en el sistema...Intente de nuevo")
#     numInt += 1
    
# if numInt <= 3:
#     print(f"Bienvenido {usr}")
# else:
#     print("Supero el numero de intentos....")

#*************************************************************

# print("Contando vocales dentro de una palabra o texto.....")
    
# vocales ="aeiou"
# palabra = input("Ingresa un texto o una palabra: ")
    
# numVoc = 0
    
# for letra in palabra:
#     if letra in vocales:
#         numVoc += 1
            
# print(f"El texto {Fore.YELLOW}{palabra}{Fore.WHITE} contiene {numVoc} vocales")

#*************************************************************

print("Invertir un texto o palabra dada por el ususario....")

frase = input("Ingrese una frase o palabra......: ")

fraseInv = ""
i = len(frase) -1

while i >= 0:
    fraseInv += frase[i]
    i -= 1
    
print(f"{Fore.YELLOW}Frase invertida👀✌: {fraseInv}{Fore.WHITE}")