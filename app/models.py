from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True, nullable=False)
    categoria = Column(String, nullable=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    valor = Column(Float, nullable=False)
    tag = Column(String, nullable=False)
    # created_at = Column(String, nullable=False)
    # 
    # updated_at = Column(String, nullable=False)  
