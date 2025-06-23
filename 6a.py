from colorama import Fore

print("*" * 90)
print(f"{Fore.YELLOW}Codigo para buscar un num en una lista {Fore.WHITE}, si se encuentra: preguntar si desea borrarlo y")
print("mencionar su posicion, si no se encuentra: preguntar si desea insertarlo")


miLista = [1,2,3,4,5,6,7,8,9,10]
miNum = int(input(f"{Fore.YELLOW}Ingrese el numero a buscar: {Fore.WHITE}"))
encontrado = False

def elimina(miNum):        
    elimina = input(f"{Fore.YELLOW}ENCONTRADO... {Fore.WHITE}Deseas eliminarlo de la lista, ingresa S o N: ")
    elimina = elimina.upper()
    if elimina == "S":
        miLista.remove(miNum)
        print(f"{miLista} El numero estaba en la posicion {indice}")
        exit()
    else:
        print("Proceso terminado, la busqueda fue exitosa")

def inserta(miNum):        
    inserta = input(f"{Fore.YELLOW}NO ENCONTRADO... {Fore.WHITE}Deseas ingresarlo a la lista, ingresa S o N: ")
    inserta = inserta.upper()
    if inserta == "S":
        miLista.append(miNum)
        print(f"{miLista} El numero se agrego a la lista")
        exit()
    else:
        print("Proceso terminado, la busqueda fue exitosa")

for elemento in miLista:
    if miNum == elemento:
        indice = miLista.index(miNum)
        encontrado = True

if encontrado == True:    
    elimina(miNum)
else:
    inserta(miNum)


        
