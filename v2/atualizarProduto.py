from entity.Produto import Produto
from sqlalchemy.orm import Session
from db.models.Product import Product


def atualizarProduto(db: Session, id_produto: int, new_nome: str, new_valor: float):
    exists = (
        db.query(Product)
        .filter(Product.id_produto == id_produto)
        .update({Product.nome: new_nome, Product.valor: new_valor})
    )
    if exists != 1:
        return {"status": 404, "message": "Esse id não existe!!"}
    else:
        db.commit()
        return {
            "status": 200,
            "message": "Produto atualizado com sucesso!!",
            "result": Produto(nome=new_nome, valor=new_valor),
        }
