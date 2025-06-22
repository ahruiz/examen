#codigo para sacar pares e impares de un rango dado

print("*" *90)
print("codigo para sacar pares e impares de un rango dado por el usuario....")

rang1 = int(input("ingresa el minimo del rango: "))
rang2 = int(input("ingresa el maximo del rango: "))
parImp = input("Ingresa P para pares o I para impares: ")
parImp = parImp.upper()

misNum = []

if parImp == "P":
    for i in range(rang1, rang2):
        if i % 2 == 0:
            misNum.append(i)
    print(f"mis numeros dentro del rango son:\n {misNum}")
    totNump = len(misNum)
    print(f"Para un total de {totNump} numeros pares")
else:
    for i in range(rang1, rang2):
        if i % 2 != 0:
            misNum.append(i)
    print(f"mis numeros dentro del rango son:\n {misNum}")
    
    totNump = len(misNum)
    print(f"Para un total de {totNump} numeros impares")
