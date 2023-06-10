def listar_produtos():
    if produtos:
        print('Esses são os produtos cadastrados atualmente:')
        for nome, valor in produtos.items():
            print(f'{nome}: R${valor:.2f}')
    
    else:
        print('Você ainda não cadastrou nenhum produto')
