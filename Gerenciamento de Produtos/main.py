from fastapi import FastAPI
from model import Produto
from db import db


app = FastAPI()


@app.get("/listar/")
def listar_produtos():
   return db

# Request Body
# isso basicamente é a passagem de valor no corpo da requisicao! nao esta sendo passado na url nem como Query Strings
@app.post("/produtos/")
def post_produtos(produto: Produto):# perceba que a varivael produto recebe a classe Produto que herda o BaseModel
    db.append(produto)
    return f"Produto: {produto.nome} com valor: {produto.valor} foi inserido com sucesso!"

# neste endpoint esta ocorrendo um requisicao para deletar p produto pelo nome no banco de dados
@app.delete("/produtos/{nome}")# o nome esta sendo passado na url
def delete_produto_nome(nome: str):# o nome passado na url esta sendo tipado como string
    for produto in db:# aqui esta acontecendo a busca do produto e remocao do mesmo
        if produto.nome == nome:
            db.remove(produto)
            return {f"O produto: {produto.nome} foi deletado!"}
        

# neste endpoint esta ocorrendo um requisicao para deletar p produto pelo nome no banco de dados
@app.delete("/produto/{id}")# o id esta sendo passado na url
def delete_produto_id(id: int):# o id passado na url esta sendo tipado como string
    for produto in db:# aqui esta acontecendo a busca do produto e remocao do mesmo
        if produto.id == id:
            db.remove(produto)
            return {f"O produto: {produto.nome} foi deletado!"}
