def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

entrada_usuario = input("Ingresa una lista de elementos separados por espacios: ")
elementos = entrada_usuario.split()

lista_invertida = invertir_lista(elementos)

print("Lista invertida:", lista_invertida)