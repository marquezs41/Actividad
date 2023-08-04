def calcular_suma_lista(lista):
    suma = sum(lista)
    return suma

entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
numeros = [float(numero) for numero in entrada_usuario.split()]

suma_total = calcular_suma_lista(numeros)

print("La suma de los números en la lista es:", suma_total)