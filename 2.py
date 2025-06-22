#codigo para sacar pares e impares de un rango dado

print("*" *90)
print("codigo para sacar pares e impares de un rango dado por el usuario....")

rang1 = int(input("ingresa el minimo del rango: "))
rang2 = int(input("ingresa el maximo del rango: "))
parImp = input("Ingresa P para pares o I para impares: ")
parImp = parImp.upper()

if parImp == "P":
    for i in range(rang1, rang2):
        if i % 2 == 0:
            print(f"....{i}")
else:
    for i in range(rang1, rang2):
        if i % 2 != 0:
            print(i)


