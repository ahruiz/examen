#abc de calificaciones por semestre
from colorama import Fore
import tabulate
import getpass
import maskpass


usuarios = {
    "admin":{
        "password" : "1234",
        "nombre" : "Administrador",
        "intentos" : 0,
        "bloqueado" : False
    }
}

numInt = 3

def limpiaPant():
    print("\n" * 10)
    
def iniciar_sess():
    limpiaPant()
    print("======== SISTEMA DE AUTENTIFICACION========")
    
    usuario = input("Usuario....: ").strip()
    
    if usuario not in usuarios:
        print(f"\n {Fore.YELLOW} Usuario no encontrado....{Fore.WHITE}")
        return False
    
    if usuarios[usuario]["bloqueado"] >= numInt:
        print(f"\n {Fore.YELLOW} Usuario bloqueado....Fv de contactar al Administrador.{Fore.WHITE}")
        return False
    
    password = maskpass.askpass("Contraseña....: ") #se pide teclear el pass y el mask manda * como echo
    #getpass.getpass("Contraseña: ")  ----> pide la contraseña sin echo
    
    if usuarios[usuario]["password"] == password:
        usuarios[usuario]["intentos"] = 0         #resetear variable intentos
        print(f"\nBienvenido {usuarios[usuario]["nombre"]}!!")
        return True
    else:
        usuarios[usuario]["intentos"] += 1
        print(f"{Fore.YELLOW}Contraseña incorrecta!!{Fore.WHITE}")
        
        if usuarios[usuario]["intentos"] >= numInt:
            usuarios[usuario]["bloqueado"] == True
            print(f"{Fore.YELLOW}\nCuenta bloqueada... contacte al Administrador!{Fore.WHITE}")
        
        return False
    
data = []

def menu_ppal():
    while True:
        print("1.- Iniciar Sesion")
        print("2.- Salir")
        opcion = input(f"{Fore.YELLOW}Seleccione una opcion: {Fore.WHITE}")
        
        if opcion == "1":
            if iniciar_sess():
                print("1.- Retiros")
                print("2.- Depositos")
                print("3.- Saldo")
                print("4.- Salir")
                
                serv = input(f"{Fore.YELLOW}Seleccione una opcion...: {Fore.WHITE}")
                if serv == "1":
                    print(f"{Fore.YELLOW} Retiro de efectivo exitoso {Fore.WHITE}")
                elif serv == "2":
                    print(f"{Fore.YELLOW}Depsito de efectivo exitoso {Fore.WHITE}")
                elif serv == "3":
                    print(f"{Fore.YELLOW}Su saldo es: $1,200.00 {Fore.WHITE}")
                else:
                    print(f"{Fore.YELLOW}Saliendo del sistema....{Fore.WHITE}")
                    break
                
        elif opcion == "2":
            print("Saliendo del sistema.....")
            break
        else:
            print("Opcion no valida. Intente nuevamente!")
                    
                
if __name__ == "__main__":
    menu_ppal()