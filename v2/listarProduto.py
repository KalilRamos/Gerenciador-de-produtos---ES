from db.models.Product import Product
from sqlalchemy.orm import Session


def listarProduto(db: Session, id_produto: int):
    produto = db.query(Product).filter(Product.id_produto == id_produto).first()
    if produto is None:
        return {"status": 404, "message": "Esse id não existe!!"}
    else:
        return {"status": 200, "result": produto}
