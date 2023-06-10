from main import app, produtos

#READ BY ID

@app.get("/produto/{id_produto}")
def listarProduto(id_produto: int):
    if id_produto > len(produtos) - 1:
        return {"status": 404, "message": "Esse id não existe!!"}
    else:
        return {"status": 200, "result": produtos[id_produto]}