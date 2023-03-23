# lê as notas do aluno e a média dos exercícios
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))
me = float(input("Digite a média dos exercícios do aluno: "))

# calcula a média de aproveitamento
ma = (n1 + n2*2 + n3*3 + me)/7

# determina o conceito correspondente à média de aproveitamento
if ma >= 9:
    conceito = "A"
elif ma >= 7.5:
    conceito = "B"
elif ma >= 6:
    conceito = "C"
elif ma >= 4:
    conceito = "D"
else:
    conceito = "E"

# imprime o resultado
print("Média de aproveitamento: %.2f" % ma)
print("Conceito: %s" % conceito)
