def alterar_produto():
    if produtos:
        nome = input("Digite o nome do produto que deseja alterar: ")
        if nome in produtos:
            print(f"Produto: {nome}")
            print(f"Valor atual: R${produtos[nome]:.2f}")

            novo_nome = input("Digite o novo nome do produto: ")
            novo_valor = input("Digite o novo valor do produto: ")

            if novo_nome != "":
                produtos[nome] = str(novo_nome)
            if novo_valor != "":
                produtos[nome] = float(novo_valor)

            print("Produto alterado com sucesso!")
        else:
            print("Produto não encontrado.")
    else:
        print("Nenhum produto cadastrado.")
