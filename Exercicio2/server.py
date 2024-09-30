from fastapi import FastAPI
from typing import List, Optional # tipagem
from pydantic import BaseModel # classe "Pai"
from uuid import uuid4 # gerador de hash automatico


app = FastAPI()

class Produto(BaseModel):
    id: Optional[int]
    nome: str
    cor: str
    preco: int


# o banco de dados é na verdade uma lista!
# os dados guardados aqui dentro sao no formato JSON
banco = []


# Listar todos os produtos 
@app.get("/produtos")
def lista_produtos():
    # retorna a lista inteira do banco de dados, em JSON
    return banco


# Cadastrar produtos
# @app.post("/produto")
@app.post("/produto/")
def criar_produto(produto: Produto):
    produto.id = str(uuid4()) # transforma o parametro id da classe produto recebe um uuid em forma de string
    banco.append(produto)


#Listar produtos pelo ID
@app.get("/produto/{produto_id}")
def obter_produtos(produto_id: str):
    for produto in banco: # percorra item a item em banco
        if produto.id == produto_id: # se 'item' com parametro 'id' for igual ao 'produto_id' passado na url
            return produto # retorne o produto inteiro, ou seja, o JSON inteiro do produto 'item
    # senao, retorne a mensagem de erro    
    return {"Erro":"Produto nao encontrado"}


# Deletar pelo ID
@app.delete("/produto/{produto_id}") # produto_id passado na url 
def deletar_id(produto_id: str): # transformado em str
    posicao = -1
    for index, produto in enumerate(banco): # percorra index e item em banco e enumere elas
        if produto.id == produto_id: # se 'item' com parametro 'id' for igual ao 'produto_id' passado na url
            posicao = index # sua posicao recebe um novo valor, o index
            break # para o for
    
    if posicao != -1: # se posicao for diferente de -1
        banco.pop(posicao) # delete no banco o item na posicao x
        return {"Mensagem":"Produto removido com sucesso!"}
    else: # senao, mostra mensagem de erro
        return {"erro":"Produto nao encontrado"}