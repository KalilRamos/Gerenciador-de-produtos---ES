produtos = {}  # Dicionário para armazenar os produtos e seus valores

def adicionar_produto():
    nome = input('Qual o nome do produto?')
    valor = float(input('Ok! Mas qual é o valor do produto?'))
    produtos[nome] = valor

while True:
    print('\n---- Menu ----')
    print('1. Cadastro de Produtos')
    print('2. sair')

    acao = input('Escolha uma das opções do menu.')

    if acao == '1':
        adicionar_produto()
    elif acao == '2':
        print('Finalizando programa...')
        break
    else:
        print('escolha uma das opções listadas')

