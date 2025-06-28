import string as s

texto = input("Introduce un texto para su analisis: ")

miLista = texto.split()

def analizar_texto(texto):
    return {
        'letras': sum(elemento in s.ascii_letters for elemento in texto),
        'dígitos': sum(elemento in s.digits for elemento in texto),
        'espacios': sum(elemento.isspace() for elemento in texto),
        'puntuacion' : sum(elemento in s.punctuation for elemento in texto),
        'longPalMasL' : max(len(elemento) for elemento in miLista),
        'palMasL' : max(miLista, key = len)
    }

print(analizar_texto(texto))  
