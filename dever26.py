palavras = input("Digite uma lista de palavras separadas por espaço: ").split()

for palavra in palavras:
    if palavra.startswith('a') or palavra.startswith('A'):
        print(palavra)
