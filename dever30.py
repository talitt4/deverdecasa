numeros = input("Digite uma lista de números separados por vírgulas: ")

# Transforma a string de números em uma lista
numeros = numeros.split(",")

# Converte cada item da lista em um número inteiro
numeros = [int(numero) for numero in numeros]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprime a lista ordenada em ordem decrescente
print("Lista ordenada em ordem decrescente:", numeros)
