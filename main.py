from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import router
import uvicorn

app = FastAPI(

    title = "Catálogo de Produtos API",
    version = "1.0.0",
    description = "API para cadastro, consulta, atualização e exclusão de produtos."

)

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

# uvicorn.run(app, host="0.0.0.0", port=8000)

