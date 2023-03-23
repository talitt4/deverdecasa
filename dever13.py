ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2023

idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar este ano!")
else:
    print("Você ainda não pode votar este ano.")
