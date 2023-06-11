from fastapi import Depends, FastAPI
from atualizarProduto import atualizarProduto
from criarProduto import criarProduto
from db.database import SessionLocal
from deletarProduto import deletarProduto
from listarProduto import listarProduto
from listarProdutos import listarProdutos
from sqlalchemy.orm import Session

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post("/produtos/{nome}/{valor}")
async def createProduct(nome: str, valor: float, db: Session = Depends(get_db)):
    return await criarProduto(db, nome, valor)


# READ
@app.get("/produtos")
def listProducts(db: Session = Depends(get_db)):
    return listarProdutos(db)


@app.get("/produto/{id_produto}")
def listProduct(id_produto: int, db: Session = Depends(get_db)):
    return listarProduto(db, id_produto)


# UPDATE
@app.put("/produto/{id_produto}/{new_nome}/{new_valor}")
def updateProduct(
    id_produto: int, new_nome: str, new_valor: float, db: Session = Depends(get_db)
):
    return atualizarProduto(db, id_produto, new_nome, new_valor)


# DELETE
@app.delete("/produto/{id_produto}")
def deleteProduct(id_produto: int, db: Session = Depends(get_db)):
    return deletarProduto(db, id_produto)