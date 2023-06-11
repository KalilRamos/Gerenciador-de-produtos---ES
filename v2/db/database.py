from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#Alterar para a suas credenciais do banco de dados
DB_URL = URL.create(
    "mysql", 
    username="root",
    password="root",
    host="localhost",
    database="project_eng_software",
)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
