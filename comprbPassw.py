#C0digo para validar generar passw seguro y validacion

print("*" * 80)
print("Genera paswword y valida......")

import random
import string as s

def generarPass():
    contPass = s.ascii_letters + s.digits + s.punctuation
    return ''.join(random.choice(contPass) for _ in range(12))
    

def validarpass(password):
    if len(password) < 12:
        return False
    
    tieneMay = any(letra in s.ascii_uppercase for letra in password)
    print(f"Cumple con el requisito de mayusculas: {tieneMay}")
    tieneMin = any(letra in s.ascii_lowercase for letra in password)
    print(f"Cumple con el requisito de minusculas: {tieneMin}")
    tieneNum = any(letra in s.digits for letra in password)
    print(f"Cumple con el requisito de numeros: {tieneNum}")
    tienePun = any(letra in s.punctuation for letra in password)
    print(f"Cumple con el requisito de Caracter especial: {tienePun}")

#    return all([tieneMay, tieneMin, tieneNum, tienePun])
    
password = generarPass()
valida = validarpass(password)
print(password)
#print(valida)

