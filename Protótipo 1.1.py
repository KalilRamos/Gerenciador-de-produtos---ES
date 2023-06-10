produtos = {}

def adicionar_produto():
    nome = input('Qual o nome do produto?')
    valor = float(input('Qual é o valor do produto?'))
    produtos[nome] = valor

def listar_produtos():
    if produtos:
        print('Esses são os produtos cadastrados atualmente:')
        for nome, valor in produtos.items():
            print(f'{nome}: R${valor:.2f}')
    
    else:
        print('Você ainda não cadastrou nenhum produto')

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

while True:
    print('\n---- Menu ----')
    print('1. Cadastro de Produtos')
    print('2. Tabela de Produtos')
    print('3. Alterar um Produto')
    print('4. Consultar Produto')
    print('5. sair')

    acao = input('Escolha uma das opções do menu.')

    if acao == '1':
        adicionar_produto()
    elif acao == '2':
        listar_produtos()
    elif acao == '3':
        alterar_produto()
    elif acao == '4':
        consultar_valor()
    elif acao == '5':
        print('Saindo...')
        break
    else:
        print('Opção inválida, escolha uma das opções do menu.')
