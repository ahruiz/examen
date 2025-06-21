#codigo para buscar un num de una lista
#si esta dar el dato y su posicion y preguntar si desea eliminarlo
#si no esta preguntar si desea agregarlo

print("*" * 90)


misNums = [1,2,3,4,5,6,7,8,9,10]
encontrado = False
numAbuscar = input("ingrese un numero a buscar: ")

for elemento in misNums:
    numAbuscar =int(numAbuscar)
    
    if numAbuscar == elemento:
        encontrado = True
        indx = misNums.index(numAbuscar)
        elimina = input("Deseas eliminarlo? ingresa S o N: ")
        elimina = elimina.upper()
        if elimina == "S":
            misNums.remove(numAbuscar)
            print(f"{misNums} estaba en el indice {indx}")
        else:
            print("Proceso terminado")
    

if encontrado == False:
    numAbuscar = int(numAbuscar)
    print(f"El numero {numAbuscar} no esta en la lista")
    inserta = input("Deseas Ingresarlo? ingresa S o N: ")
    inserta = inserta.upper()
    if inserta == "S":
        misNums.append(numAbuscar)
        print(misNums)
        exit()
        

