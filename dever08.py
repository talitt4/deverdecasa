# pede para o usuário digitar o valor de X
x = int(input("Digite o valor de X: "))

# loop para desenhar as linhas do pinheiro
for i in range(1, x*2, 2):
    print((" " * (x - i // 2)) + ("X" * i))

# desenha o tronco do pinheiro
for i in range(2):
    print((" " * (x-1)) + "XX")
    print((" " * (x-2)) + "XXXX")
