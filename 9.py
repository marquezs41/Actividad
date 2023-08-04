def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

def generar_matriz(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    return matriz

num_filas = int(input("Ingresa el número de filas: "))
num_columnas = int(input("Ingresa el número de columnas: "))

matriz_generada = generar_matriz(num_filas, num_columnas)

print("Matriz generada:")
imprimir_matriz(matriz_generada)