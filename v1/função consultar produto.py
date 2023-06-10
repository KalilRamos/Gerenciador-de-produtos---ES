def consultar_valor():
    if produtos:
        nome = input("Digite o nome do produto a ser consultado: ")
        if nome in produtos:
            print(f"Produto: {nome}")
            print(f"Valor: R${produtos[nome]:.2f}")
        else:
            print("Produto não encontrado.")
    else:
        print("Nenhum produto cadastrado.")