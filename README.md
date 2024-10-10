
# Exercicios/Anotações/Testes/Ideias

Repositório dedicado para a prática e anotações de exercicios para fixação de conteúdo.



## Observação

Nos códigos a seguir não existe clean code.


## Rodando localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto](https://github.com/Rodrigo-Kelven/Exercicios_FastAPI
```

Entre em um dos diretórios do projeto

```bash
  cd Exercicio*
```

Instale venv  'se preferir'

```bash
  python3 -m venv 'nome da venv'

  Exemplo: python3 -m venv venv
```
Utilise a venv  'se preferir'

```bash
  Windowns: .\venv\Scripts\activate
  Linux: source venv/bin/activate
```
Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  uvicorn main:app --reload
    
