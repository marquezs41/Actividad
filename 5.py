import random


cantidad_numeros = int(input("Ingresa la cantidad de números aleatorios a generar: "))
valor_minimo = int(input("Ingresa el valor mínimo para los números aleatorios: "))
valor_maximo = int(input("Ingresa el valor máximo para los números aleatorios: "))

lista_aleatoria = [random.randint(valor_minimo, valor_maximo) for _ in range(cantidad_numeros)]

print("Lista de números aleatorios:", lista_aleatoria)