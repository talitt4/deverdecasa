elif opcao == 4:
    print("Opção escolhida: Consultar")
    id_cliente = int(input("Digite o ID do cliente: "))
    if id_cliente in clientes:
        print("Cliente encontrado:")
        print(f"Nome: {clientes[id_cliente]['nome']}")
        print(f"Email: {clientes[id_cliente]['email']}")
    else:
        print("Cliente não encontrado!")
