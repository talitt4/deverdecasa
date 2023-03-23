import math

num_lados = int(input("Digite o número de lados do polígono regular: "))

if num_lados == 3:
    lado = float(input("Digite o valor do lado do triângulo em metros: "))
    area = (lado ** 2) * math.sqrt(3) / 4
    print(f"TRIÂNGULO com área de {area:.2f} m²")
elif num_lados == 4:
    lado = float(input("Digite o valor do lado do quadrado em metros: "))
    area = lado ** 2
    print(f"QUADRADO com área de {area:.2f} m²")
elif num_lados == 5:
    print("PENTÁGONO")
else:
    print("Polígono não identificado.")
