from pydantic import BaseModel, EmailStr

# Porque Usar o Pydantic? Isto serve para manipular os contratos entre as requisições
# Não confunda com ORM, ORM's serve para manupular banco de dados
# Mas o que é isso? Isso é basicamente um MODELO para os dados que você quiser, veja os exemplos abaixo

# Apartir de agora fale e entenda que isso é um Modelo!

# Modelo de mensagem
class Mensagem(BaseModel):
    message: str


# Modelo de Users
class Users(BaseModel):
    username: str
    email: EmailStr
    password: str

# Modelo que adiciona um id a cada usuario e herda de User suas propriedades
class UserDB(Users):
    id: int

# Modelo de resposta usado para responder, para que o usuario veja suas informações que foram enviadas
class UsersPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

# Modelo usado para listar todos os usuarios cadastrados no database
class UserList(BaseModel):
    users: list[UsersPublic]