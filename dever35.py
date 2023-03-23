numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

# converte os números de string para inteiros
numeros = [int(num) for num in numeros]

# remove os números duplicados
numeros_sem_duplicados = list(set(numeros))

# imprime a lista sem os números duplicados
print("Lista sem números duplicados: ")
print(numeros_sem_duplicados)
