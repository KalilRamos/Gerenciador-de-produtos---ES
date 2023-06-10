from main import app, produtos

#DELETE

@app.delete("/produto/{id_produto}")
def deleteProduto(id_produto: int):
    if id_produto > len(produtos) - 1:
        return {"status": 404, "message": "Esse id não existe!!"}
    else:
        produtos.pop(id_produto)
        return {
            "status": 200,
            "message": "Produto deletado com sucesso!!",
            "result": produtos,
        }