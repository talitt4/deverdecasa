nomes = input("Digite uma lista de nomes separados por vírgulas: ")

# Transforma a string de nomes em uma lista
nomes = nomes.split(",")

# Remove espaços em branco no início e fim de cada nome
nomes = [nome.strip() for nome in nomes]

# Encontra o nome mais longo e o nome mais curto da lista
mais_longo = max(nomes, key=len)
mais_curto = min(nomes, key=len)

# Imprime o nome mais longo e o nome mais curto da lista
print("Nome mais longo: ", mais_longo)
print("Nome mais curto: ", mais_curto)
