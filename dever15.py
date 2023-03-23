altura = float(input("Digite a altura da pessoa em metros: "))
sexo = int(input("Digite o sexo da pessoa (1 para feminino ou 2 para masculino): "))

if sexo == 1:
    peso_ideal = 62.1 * altura - 44.7
elif sexo == 2:
    peso_ideal = 72.7 * altura - 58
else:
    print("Sexo inválido.")
    exit()

print(f"O peso ideal para uma pessoa de {altura}m de altura e sexo {sexo} é {peso_ideal:.2f}kg.")
