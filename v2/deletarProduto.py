from sqlalchemy.orm import Session
from db.models.Product import Product


def deletarProduto(db: Session, id_produto: int):
    produto = db.query(Product).filter(Product.id_produto == id_produto).first()
    if produto is None:
        return {"status": 404, "message": "Esse id não existe!!"}
    else:
        db.query(Product).filter(Product.id_produto == id_produto).delete()
        db.commit()
        return {
            "status": 200,
            "message": "Produto deletado com sucesso!!",
            "result": db.query(Product).all(),
        }
