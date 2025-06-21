#codigo para convertir grados C a F y viceversa
#con ambos datos dados por el usr

print("*" * 90)
print("Codigo para convertir grados C a F y viceversa capturados por el usuario")

temp = float(input("Ingresa los grados que quieres convertir: "))
conv = input("Ingresa F para C->F... C para F->C: ") 

if conv == "F":
    graFar = temp * (9/5) + 32
    print(f"La conversion de {temp} grados Centigrados es: {graFar} Farenheit")
else:
    graCent = (temp - 32) * (5/9)
    print(f"La conversion de {temp} grados farenheit es: {graCent} Centigrados")

    