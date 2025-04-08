from pydantic import BaseModel, Field
from typing import Optional

class ProdutoBase(BaseModel):
    codigo: str
    nome: str
    descricao: Optional[str] = None
    valor: float = Field(gt=0, description="O valor do produto deve ser maior que zero.")
    tag: str


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(ProdutoBase):
    pass


class ProdutoOut(ProdutoBase):
    id: int

    class Config:
        orm_mode = True
        