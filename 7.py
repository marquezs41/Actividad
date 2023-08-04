def encontrar_maximo(lista):
    maximo = max(lista)
    return maximo
def encontrar_minimo(lista):
    minimo = min(lista)
    return minimo

entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
numeros = [float(numero) for numero in entrada_usuario.split()]

numero_maximo = encontrar_maximo(numeros)

numero_minimo = encontrar_minimo(numeros)

print("El número más grande en la lista es:", numero_maximo)
print("El número más pequeño en la lista es:", numero_minimo)