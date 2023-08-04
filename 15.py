def es_palindromo(cadena):
    cadena = cadena.lower() 
    cadena = ''.join(c for c in cadena if c.isalnum())  
    return cadena == cadena[::-1]

cadena_ingresada = input("Ingresa una cadena de texto: ")

if es_palindromo(cadena_ingresada):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")