from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix ="/produtos", tags = ["produtos"])

# dependency para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@router.post("/", response_model = schemas.ProdutoOut, status_code=201)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = crud.get_produto_por_codigo(db, produto.codigo)
    if db_produto:
        raise HTTPException(status_code=400, detail="Já existe um produto com esse código")
    return crud.criar_produto(db, produto)


@router.get("/", response_model=list[schemas.ProdutoOut])
def listar_produtos(db: Session = Depends(get_db)):
    return crud.get_produtos(db)


@router.get("/{codigo}", response_model=schemas.ProdutoOut)
def obter_produto(codigo: str, db: Session = Depends(get_db)):
    produto = crud.get_produto_por_codigo(db, codigo)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@router.put("/{codigo}", response_model=schemas.ProdutoOut)
def atualizar_produto(codigo: str, produto: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    atualizado = crud.atualizar_produto(db, codigo, produto)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return atualizado


@router.delete("/{codigo}", status_code=204)
def deletar_produto(codigo: str, db: Session = Depends(get_db)):
    deletado = crud.deletar_produto(db, codigo)
    if not deletado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")