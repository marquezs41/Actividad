def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

numero_ingresado = int(input("Ingresa un número para calcular su factorial: "))

factorial_calculado = calcular_factorial(numero_ingresado)

print("El factorial de", numero_ingresado, "es:", factorial_calculado)






