numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

# converte os números de string para inteiros
numeros = [int(num) for num in numeros]

# imprime apenas os números maiores do que 10
print("Números maiores do que 10: ")
for num in numeros:
    if num > 10:
        print(num)
