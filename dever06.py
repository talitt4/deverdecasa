opcao = -1

while opcao != 0:
    print("Cadastro de Clientes")
    print("0 - Fim")
    print("1 - Inclui")
    print("2 - Altera")
    print("3 - Exclui")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Programa encerrado!")
    elif opcao == 1:
        print("Opção escolhida: Incluir")
        # implementar a lógica de inclusão de clientes aqui
    elif opcao == 2:
        print("Opção escolhida: Alterar")
        # implementar a lógica de alteração de clientes aqui
    elif opcao == 3:
        print("Opção escolhida: Excluir")
        # implementar a lógica de exclusão de clientes aqui
    else:
        print("Opção inválida! Tente novamente.")
