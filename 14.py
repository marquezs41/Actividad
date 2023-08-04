def calcular_media_aritmetica(lista):
    total = sum(lista)
    cantidad_elementos = len(lista)
    media = total / cantidad_elementos
    return media

entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
numeros = [float(numero) for numero in entrada_usuario.split()]

media_calculada = calcular_media_aritmetica(numeros)

print("La media aritmética de los números es:", media_calculada)