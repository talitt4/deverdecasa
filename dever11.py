n = int(input("Digite o número de termos da PA: "))
a1 = float(input("Digite o valor inicial da PA: "))
an = float(input("Digite o valor final da PA: "))

# Calculando a soma da PA
soma = n * (a1 + an) / 2

# Mostrando o resultado na tela
print("A soma dos {} termos da PA é igual a {:.2f}".format(n, soma))
