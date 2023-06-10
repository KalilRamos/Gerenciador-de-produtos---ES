#READ
from main import app, produtos

@app.get("/produtos")
def listarProdutos():
    return {"Produtos": produtos}