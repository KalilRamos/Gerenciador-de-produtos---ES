from sqlalchemy import Column, Float, Integer, String
from db.database import Base


class Product(Base):
    __tablename__ = "produtos"

    id_produto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    valor = Column(Float, index=True)