# 📦 Catálogo de Produtos API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)


API RESTful para cadastro, consulta, atualização e exclusão de produtos. Desenvolvida em Python com FastAPI, com validações de regras de negócio, testes automatizados, documentação via Swagger e containerização com Docker.

## 🚀 Funcionalidades

- Cadastro de produtos com os seguintes campos:
  - Código único (obrigatório)
  - Nome (obrigatório)
  - Descrição
  - Valor (deve ser maior que R$ 0)
  - Tag de categoria (obrigatória, enviada como texto)
- Consulta de:
  - Todos os produtos
  - Produto específico pelo código
  - Produtos agrupados por tag
- Atualização e exclusão de produtos
- Validações de regras de negócio


## 📚 Regras de Negócio

- Código, nome e tag são campos obrigatórios.
- O valor do produto deve ser maior que R$ 0.
- Tags são strings usadas para categorizar e agrupar produtos.
- Códigos de produtos são únicos no sistema.


## 🛠️ Tecnologias utilizadas

- Python 3.10+
- FastAPI
- SQLite
- SQLAlchemy
- Pytest
- Docker + Docker Compose
- Swagger (OpenAPI)

## 📄 Documentação

Após iniciar o projeto, acesse a documentação interativa:

[http://localhost:8000/docs](http://localhost:8000/docs)

## 📦 Instalação e execução local (sem Docker)

1. Crie o ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

2. Instale as dependências:

pip install -r requirements.txt

3. Rode a aplicação:

uvicorn app.main:app --reload
