from sqlalchemy.orm import Session
from sqlalchemy import func 
from app import models,schemas
import re


# def get_produtos_por_prefixo(db: Session, codigo: str):
#     codigo_limpo = re.sub(r"[^a-zA-Z0-9]", "", codigo).upper()
#     like_pattern = f"{codigo_limpo}%"
#     print(f"BUSCANDO POR: {codigo_limpo} LIKE {like_pattern}")
    
#     return db.query(models.Produto).filter(
#         func.upper(func.replace(models.Produto.codigo, "-", "")).like(like_pattern)
#     ).all()


def get_produtos_por_prefixo(db: Session, codigo: str):
    codigo_input = re.sub(r"[^a-zA-Z0-9]", "", codigo).upper()

    codigo_db = func.replace(func.upper(models.Produto.codigo), "-", "")

    return db.query(models.Produto).filter(
        codigo_db.like(f"{codigo_input}%")
    ).all()

def get_produtos_por_codigo(db: Session, codigo: str):
    return db.query(models.Produto).filter(
        func.upper(models.Produto.codigo) == codigo.upper()).all()


def get_produto_por_codigo(db: Session, codigo: str):
    return db.query(models.Produto).filter(models.Produto.codigo == codigo).first()


def get_produtos(db: Session):
    return db.query(models.Produto).all()

def get_produtos_agrupados_por_tag(db:Session):
    produtos = db.query(models.Produto).all()
    agrupado = {}

    for produto in produtos:
        agrupado.setdefault(produto.tag, []).append(produto)

    return agrupado

def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto = models.Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto
    
def atualizar_produto(db:Session, codigo: str, dados: schemas.ProdutoUpdate):
    produto = get_produto_por_codigo(db, codigo)
    if produto:
        for key, value in dados.model_dump().items():
            setattr(produto, key,value)
        db.commit()    
        db.refresh(produto)

    return produto

def deletar_produto(db:Session, codigo: str):
    produto = get_produto_por_codigo(db, codigo)
    if produto:
        db.delete(produto)
        db.commit()

    return produto