# DESAFIO HYPERATIVA (Credit Card API) 

## Setup Local

## Nota do desenvolvedor 

Este projeto foi criado com o auxilio de ferramentas LLMs como chatgpt e Gemini.

Utilizei estas ferramentas, em um projeto de avaliação, porque acredito que são fabulosas ferramentas para desenvolvimento de sistemas.

O uso dessas ferramentas não desonera o papel do desenvolvedor, que se mantém crucial para definir estratégias, escrever prompts eficazes, resolver problemas com criatividade, organizar diretórios e arquivos,realizar testes garantindo a qualidade do aplicativo e   por fim deployments e manipulação de repositórios Git.

# Credit Card API

## Setup Local

1. Clone o repositório:
    ```bash
    git clone git@github.com:NelioJunior/desafio_hyperativa.git
    cd credit_card_api
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `.env`:
    ```plaintext
    SECRET_KEY= Entre com sua senha 
    DATABASE_URL = sqlite:///app.db
    JWT_SECRET_KEY =  Entre com sua senha JWT 
    ```

5. Inicialize o banco de dados:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Execute a aplicação:
    ```bash
    flask run
    ```

7. A aplicação estará disponível em `http://127.0.0.1:5000`.

## Endpoints da API

### Registro de Usuário

- **URL:** `/register`
- **Método:** `POST`
- **Descrição:** Registra um novo usuário.
- **Exemplo de Requisição:**
    ```json
    {
        "username": "user",
        "password": "senha"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Usuário criado com sucesso"
    }
    ```
- **Código de Resposta:** `201 Created`
- **Erros Possíveis:**
    - `400 Bad Request` se o usuário já existe.

### Login de Usuário

- **URL:** `/login`
- **Método:** `POST`
- **Descrição:** Faz login e retorna um token JWT.
- **Exemplo de Requisição:**
    ```json
    {
        "username": "usuario tester",
        "password": "senha"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "access_token": "jwt_token"
    }
    ```
- **Código de Resposta:** `200 OK`
- **Erros Possíveis:**
    - `401 Unauthorized` se as credenciais forem inválidas.

### Adicionar Número de Cartão

- **URL:** `/add_card`
- **Método:** `POST`
- **Descrição:** Adiciona um novo número de cartão.
- **Requer Autenticação:** Sim (Bearer Token)
- **Exemplo de Requisição:**
    ```json
    {
        "card_number": "1234567812345678"
    }
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Cartão adicionado com sucesso"
    }
    ```
- **Código de Resposta:** `201 Created`
- **Erros Possíveis:**
    - `400 Bad Request` se o cartão já existe.

### Verificar Número de Cartão

- **URL:** `/check_card/<card_number>`
- **Método:** `GET`
- **Descrição:** Verifica se um número de cartão existe.
- **Requer Autenticação:** Sim (Bearer Token)
- **Exemplo de Requisição:**
    - `GET /check_card/1234567812345678`
- **Resposta de Sucesso:**
    ```json
    {
        "card_id": 1
    }
    ```
- **Código de Resposta:** `200 OK`
- **Erros Possíveis:**
    - `404 Not Found` se o cartão não existe.

### Adicionar Números de Cartão a Partir de Arquivo

- **URL:** `/add_cards_from_file`
- **Método:** `POST`
- **Descrição:** Adiciona números de cartão a partir de um arquivo TXT.
- **Requer Autenticação:** Sim (Bearer Token)
- **Exemplo de Requisição:**
    - utilizando o arquivo `DESAFIO-HYPERATIVA.txt` 
        ```
    - Executar no terminal `curl`:
        ```bash
        curl -X POST -H "Authorization: Bearer <jwt_token>" -F "file=@DESAFIO-HYPERATIVA.txt" http://127.0.0.1:5000/add_cards_from_file
        ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Cards added successfully from file"
    }
    ```
- **Código de Resposta:** `201 Created`

### Adicionar Números de Cartão a Partir de Arquivo Personalizado

- **URL:** `/add_cards_from_custom_file`
- **Método:** `POST`
- **Descrição:** Adiciona números de cartão a partir de um arquivo TXT no formato personalizado.
- **Requer Autenticação:** Sim (Bearer Token)

    - Usando `curl`:
        ```bash
        curl -X POST -H "Authorization: Bearer <jwt_token>" -F "file=@DESAFIO-HYPERATIVA.txt" http://127.0.0.1:5000/add_cards_from_custom_file
        ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Cards added successfully from custom file"
    }
    ```
- **Código de Resposta:** `201 Created`

## Executar Testes

Para executar os testes unitários:
```bash
python -m unittest discover -s tests
