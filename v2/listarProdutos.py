from sqlalchemy.orm import Session
from db.models.Product import Product

def listarProdutos(db: Session):
    produtos = db.query(Product).all()
    return {"Produtos": produtos}
