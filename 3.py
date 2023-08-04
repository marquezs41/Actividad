import random

def generar_lista_aleatoria(n, minimo, maximo):
    lista = [random.randint(minimo, maximo) for _ in range(n)]
    return lista

cantidad_numeros = int(input("Ingresa la cantidad de números aleatorios a generar: "))
valor_minimo = int(input("Ingresa el valor mínimo para los números aleatorios: "))
valor_maximo = int(input("Ingresa el valor máximo para los números aleatorios: "))

lista_aleatoria = generar_lista_aleatoria(cantidad_numeros, valor_minimo, valor_maximo)

print("Lista de números aleatorios:", lista_aleatoria)