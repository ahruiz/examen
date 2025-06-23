from colorama import Fore

try:
    milista = []
    r = int(input("ingresa un numero para sacar sus numeros pares e impares hasta ese num: "))
    q = input(f"{Fore.YELLOW} ingresa A: ambos, P:pares o I:impares...: {Fore.WHITE}")
    q = q.upper()

    if q == "A" or q == "P" or q == "I":
        def numP(r):
            for i in range(r):
                if i % 2 == 0:
                    milista.append(i)
                    longMiLista = len(milista)
            print(milista)
            print(f"Mi lista contiene {longMiLista} numeros pares")
            milista.clear()

        def numI(r):
            for i in range(r):
                if i % 2 != 0:
                    milista.append(i)
                    longMiLista = len(milista)
            print(milista)
            print(f"Mi lista contiene {longMiLista} numeros impares")
            
        if q == "A":
            numP(r)
            numI(r)
        elif q == "P":
            numP(r)
        else:
            numI(r)
    else:
        print("Ingresaste datos incorrectos....intenta de nuevo.")
except:
    print("Debes INGRESAR solo datos numericos enteros.....intenta de nuevo")