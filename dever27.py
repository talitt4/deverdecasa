# Solicita ao usuário uma lista de números
numeros = input("Digite uma lista de números separados por vírgulas: ")

# Separa os números em uma lista
numeros = numeros.split(",")

# Converte cada número na lista para um número inteiro
numeros = [int(numero) for numero in numeros]

# Encontra o número máximo e mínimo da lista
maximo = max(numeros)
minimo = min(numeros)

# Exibe os resultados
print("O número máximo é:", maximo)
print("O número mínimo é:", minimo)
