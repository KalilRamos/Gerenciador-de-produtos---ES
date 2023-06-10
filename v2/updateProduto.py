from main import app, produtos

#UPDATE

@app.put("/produto/{id_produto}/{new_nome}/{new_valor}")
def updateProduto(id_produto: int, new_nome: str, new_valor: float):
    if id_produto > len(produtos) - 1:
        return {"status": 404, "message": "Esse id não existe!!"}
    else:
        produtos[id_produto] = Produto(nome=new_nome, valor=new_valor)
        return {
            "status": 200,
            "message": "Produto atualizado com sucesso!!",
            "result": produtos[id_produto],
        }