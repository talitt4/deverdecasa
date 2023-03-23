a1 = float(input("Digite o valor inicial (a1): "))
n = int(input("Digite a quantidade de termos (n): "))
q = float(input("Digite a razão (q >= 2): "))

if q < 2:
    print("A razão deve ser maior ou igual a 2!")
else:
    Sn = a1 * (q**n - 1) / (q - 1)
    print("O valor da soma da sequência é:", Sn)
