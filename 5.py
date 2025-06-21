print("Calculadora para dos numeros seleccionando operacion:")
print("suma... Teclea S")
print("resta... Teclea R")
print("multiplicar... Teclea M")
print("Dividir... Teclea D")
print("Residuo... Teclea RE")
print("potencia... Teclea P")

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el el segundo numero numero: "))
oper = input("ingresa la operacion que deseas realizar: ")

oper = oper.upper()

match oper:
    case "S":
        suma = num1 + num2
        print(f"La suma de los numeros es {suma}")
    case "R":
        resta = num1 - num2
        print(f"La resta de los numeros es {resta}")
    case "M":
        mult = num1 * num2
        print(f"La multiplicacion de los numeros es {mult}")
    case "D":
        div = num1 / num2
        if num2 == 0:
            print("La division entre cero no es valida")
        else:
            print(f"La division de los numeros es {div}")
    case "RE":
        resi = num1 % num2
        print(f"El residuo de la div entre los numeros es {resi}")
    case "P":
        potn = num1 ** num2
        print(f"La potencia de los numeros es {potn}")        