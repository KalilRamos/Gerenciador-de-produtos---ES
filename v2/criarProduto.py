# CREATE
from db.models.Product import Product
from entity.Produto import Produto
from sqlalchemy.orm import Session


async def criarProduto(db: Session, nome: str, valor: float):
    db.add(Product(nome=nome, valor=valor))
    db.commit()
    return {
        "status": 200,
        "message": "Produto adicionado com sucesso!!",
        "result": Produto(nome, valor),
    }
