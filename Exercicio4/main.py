from fastapi import FastAPI, HTTPException
from schema import Mensagem, Users, UsersPublic, UserDB, UserList
from database import database 

# Dicas para entender melhor:
"""
1 - Documentar/Documentaçao => documentar, entenda que sera tudo aquilo que o fastapi irá lhe mostrar na rota /docs | documentação sera pque esta sendo documentado
2 - Sempre olhe o nome do modelo em schema.py porque o nome da classe/Modelo do respectivo response_model=  nao pode ser diferente, veja a linha 25 e 27
"""


app = FastAPI()

# Rota Home
@app.get("/", response_model=Mensagem)
def home(nome: str = "Mundo"):
    texto = {
        "nome":f"{nome.capitalize()}",
    }
    return {"message":f"{texto}"}


# Rota para listar usuarios
# este response_model recebe um Modelo onde seu parametro é users, se "users" da linha 29 for alterado, o codigo quebra, porque o response_model é o "retorno visualizado" la na documentacao => /docs
@app.get("/users/", response_model=UserList)# resumindo, se for usar response_model faça de uma forma que não precise alterar, SE ALTERAR DA PROBELMA
def listar_usuarios():
    return {"users": database}



# Exemplo 1
# Rota para criar users 
@app.post("/users/{nome}/{email}")# nesta url, voce deve/required passar os parametros que obedecan a funcao, isso será 'DOCUMENTADO' em /docs
def create_users_1(nome: str, email: str, senha: str = 123):# tudo aqui dentro da função será documentado e será a documentação em /docs

    resultado = {"Nome":f"{nome}",
                 "Email":f"{email}",
                 "Senha":f"{senha}",
                 }
    database.append(resultado)
    return database



# Exemplo 2
# Rota para criar users 

# porque aqui não precisa passar nenhum parametro na url, nem como Query Strings ? Porque a resposta será passada em forma de corpo, Body
# aqui voce percebe que a varivel users está sendo associada ao Objeto/Modelo Users, então o FastApi com sua 'magia' irá DOCUMENTAR isso, que será passado como Body Request
# então para usar este enpoint, voce terá que satisfazer esse modelo, enviando os dados que existem dentro do modelo Users, resumindo, vai ter que mandar os dados que o modelo possui!

@app.post("/users/", response_model=UsersPublic,status_code=201) # este response_model é a EXIBIÇÃO na documentação, da resposta que será enviada, ele recebe o MODELO onde não mostra o password
#  Users => contrato de modelo de entrada
#  UsersPublic => contrato de modelo de saida
def create_users_2(users: Users): # mas, users está associado/recebendo um modelo que para ser enviado corretamente no corpo da requisição/Request Body, precisa da senha/password

    user_with_id = UserDB(
        id=len(database) + 1,
        **users.model_dump()
    )
    
    database.append(user_with_id)
    return user_with_id


# Rota para atualizar usuario
@app.put("/users/{user_id}", response_model=UsersPublic)
def update_user(user_id: int, user: Users):
    # se o id do usuario for menor que 1 ou maior que o tamanho do database
    # error not found!
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail="User Not Found!")
    # substitui um dado pelo outro
    user_with_id = UserDB(id = user_id, **user.model_dump())
    database[user_id - 1 ] = user_with_id
    return user_with_id


# Rota para deletar
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=404, detail="User not Found!")
    
    del database[user_id - 1]
    return {"Mensagem": "Usuario deletado!"}

