# pede ao usuário para digitar uma lista de números
lista_str = input("Digite uma lista de números separados por espaço: ")

# converte a lista de strings em uma lista de inteiros
lista = [int(num) for num in lista_str.split()]

# imprime apenas os números pares da lista
print("Números pares da lista:")
for num in lista:
    if num % 2 == 0:
        print(num)
