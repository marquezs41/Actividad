numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
print("Suma:", suma)

resta = numero1 - numero2
print("Resta:", resta)

multiplicacion = numero1 * numero2
print("Multiplicación:", multiplicacion)

if numero2 != 0:
    division = numero1 / numero2
    print("División:", division)
else:
    print("No se puede dividir por cero.")