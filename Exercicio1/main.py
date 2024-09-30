from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# rota normal sem passagem de parametros
@app.get("/")
def index():
    return {"ola":"mundo"}

# duas rotas que respondem ao mesmo chamado, so que uma delas exige a passagem de parametros
@app.get("/ola/")
@app.get("/ola/{nome}")
def ola(nome="world"):
    return {f"Ola {nome},":"tudo bem?"}

# esta rota sim exige a passagem de parametros
@app.get("/area-quadrado/{largura}/{altura}")# os paraemtros sao passados na própria url
def area(largura: int, altura: int):
    resultado = largura * altura
    texto = f"O resultado de {largura} de largura e {altura} de altura é: {resultado}"
    return texto


# nesta rota, os parametros sao passados na url como query string => "/area/?largura=5&altura=6"
@app.get("/area/")
def area(largura: int, altura: int):# largura e altura so recebem numeros inteiros
    resultado = largura * altura
    texto = f"O resultado de {largura} de largura e {altura} de altura é: {resultado}"
    return texto



# esta classe esta herdando de Base Model
# esta classe tem atributos nome como string e preco como float
class Produto(BaseModel):
    nome: str
    preco: float    

# nao há a passagem de parametros na url
# os parametros sao passados como JSON. no corpo da requisicao, no body
@app.post("/produtos/")
def produtos(produto: Produto):# a variavel produto recebe a classe e seus atributos para poder acessa-los e mostra-los
    return {"mensagem":f"Produto: ({produto.nome} - R$ {produto.preco}) Foi cadastrado com sucesso!"}