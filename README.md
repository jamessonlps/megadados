# API RESTfull


Essa API trata-se de um microsserviço de controle de estoque.

Para executar:

- Crie um banco de dados no `MYSQL`
- Adicione os dados de acesso ao banco em um arquivo `.env`, conforme o exemplo deixado em `example.env`
- Crie um ambiente virtual
- Instale as dependências:

```
pip install -r requirements.txt
```

- Execute o script deixado em `./scripts` no `MYSQL` para montar o banco de dados
- Execute a API
```
uvicorn main:app --reload
```
- Acesse a documentação: http://127.0.0.1:8000/docs#/