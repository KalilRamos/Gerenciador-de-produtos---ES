from v2.Produto import Produto

from v2.main import app, produtos


@app.post("/produtos/{nome}/{valor}")
def criarProduto(nome: str, valor: float):
    produto = Produto(nome, valor)
    produtos.append(produto)
    return {
        "status": 200,
        "message": "Produto adicionado com sucesso!!",
        "result": produto,
    }