from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Explicações


# app recebe tudo da classe FastAPI()
# app recebe um tipo de método http, o método get()
# este método precisa de parametros, como rotas e outros parametros inseridos na propria url
# quando acessada essa rota via metodo getn retorna oque a funçao conter
@app.get('/')
def home():
    return {"Hello":"World"}


# nesta rota, percebe-se que esta sendo passado um parametro {nome}
# este parametro pode ser inserido como /ola/Rodrigo
@app.get('/ola/{nome}')
def ola(nome: str): # aqui está sendo definido o tipo do parametro => {nome} que está sendo passado na url
    return {f"Ola {nome}":"tubo bem?"} # retornando assim Ola Rodrigo tudo bem?


# aqui nao é tao diferente mas é importante aprender
# aqui não esta sendo pedido nenhum parametro na rota
# a função: => def index() | 
#   {está configurando/setando o tipo de parametro que deverá ser se for inserido um parametro e,
#    ao mesmo tempo, está com um parametro como padrao/default se nenhum paraemtro for passado}
@app.get('/ola/')
def index(nome: str = "Valor padrão/default"):
    return {f"Ola {nome}":"tubo bom?"}


class Produtos(BaseModel):
    nome: str
    valor: int

db = []

@app.post('/produto/')
def inserir_produtos(produto: Produtos):
    db.append(produto)

@app.get('/produtos/')
def listar():
    return db

@app.get('/produtos/{id_nome}')
def listar_p_id(id_nome: str):
    for p in db:
        if p.nome == id_nome:
            return p
        
@app.delete('/produto/{p_nome}')
def dell(p_nome: str):
    for p in db:
        if p.nome == p_nome:
            db.remove(p)
            return "Removido"