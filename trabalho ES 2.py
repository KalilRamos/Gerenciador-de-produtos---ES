produtos = {}  # Dicionário para armazenar os produtos e seus valores

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

while True:
    print('\n---- Menu ----')
    print('1. Cadastro de Produtos')
    print('2. Tabela de Produtos')
    print('3. sair')

    acao = input('Escolha uma das opções do menu.')

    if acao == '1':
        adicionar_produto()
    elif acao == '2':
        listar_produtos()
    elif acao == '3':
        print('Saindo...')
        break
    else:
        print('Por favor, escolha uma das opções do menu.')