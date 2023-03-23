numeros = input("Digite uma lista de números separados por espaço: ")
numeros = numeros.split()

# converte os números de string para inteiros
numeros = [int(num) for num in numeros]

# imprime apenas os números menores do que 5
print("Números menores do que 5: ")
for num in numeros:
    if num < 5:
        print(num)
