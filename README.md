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

2. Coloque o arquivo `DESAFIO-HYPERATIVA.txt` no diretório raiz do projeto.

3. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure as variáveis de ambiente no arquivo `.env`:
    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URL=sqlite:///app.db
    JWT_SECRET_KEY=your_jwt_secret_key
    ```

6. Inicialize o banco de dados:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

7. Execute a aplicação:
    ```bash
    flask run
    ```

8. A aplicação estará disponível em `http://127.0.0.1:5000`.

## Endpoints da API

### Registro de Usuário

- **URL:** `/register`
- **Método:** `POST`
- **Descrição:** Registra um novo usuário.
- **Exemplo de Requisição:**
    ```bash
    curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password"}'
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
    ```bash
    TOKEN=$(curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password"}' | jq -r .access_token)
    ```
- **Resposta de Sucesso:**
    ```json
    {
        "access_token": "seu_token_jwt_aqui"
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
    ```bash
    curl -X POST http://127.0.0.1:5000/add_card -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d '{"card_number": "1234567812345678"}'
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
    - Enviar um arquivo `cards.txt` com o seguinte conteúdo:
        ```
        1234567812345678
        8765432187654321
        ```
    - Usando `curl`:
        ```bash
        curl -X POST -H "Authorization: Bearer $TOKEN" -F "file=@cards.txt" http://127.0.0.1:5000/add_cards_from_file
        ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Cartões adicionados com sucesso a partir do arquivo"
    }
    ```
- **Código de Resposta:** `201 Created`

### Adicionar Números de Cartão a Partir de Arquivo Personalizado

- **URL:** `/add_cards_from_custom_file`
- **Método:** `POST`
- **Descrição:** Adiciona números de cartão a partir de um arquivo TXT no formato personalizado.
- **Requer Autenticação:** Sim (Bearer Token)
- **Exemplo de Requisição:**
    - Enviar um arquivo `DESAFIO-HYPERATIVA.txt`
        ```
    - Executar pelo terminal `curl`:
        ```bash
        curl -X POST -H "Authorization: Bearer $TOKEN" -F "file=@DESAFIO-HYPERATIVA.txt" http://127.0.0.1:5000/add_cards_from_custom_file
        ```
- **Resposta de Sucesso:**
    ```json
    {
        "message": "Cartões adicionados com sucesso a partir do arquivo personalizado"
    }
    ```
- **Código de Resposta:** `201 Created`

### Listar Usuários

- **URL:** `/users`
- **Método:** `GET`
- **Descrição:** Lista todos os usuários registrados.
- **Requer Autenticação:** Sim (Bearer Token)
- **Exemplo de Requisição:**
    - Usando `curl`:
        ```bash
        curl -X GET http://127.0.0.1:5000/users -H "Authorization: Bearer $TOKEN"
        ```
- **Resposta de Sucesso:**
    ```json
    [
        {
            "id": 1,
            "username": "testuser"
        }
    ]
    ```
- **Código de Resposta:** `200 OK`

### Listar Cartões

- **URL:** `/cards`
- **Método:** `GET`
- **Descrição:** Lista todos os cartões registrados.
- **Requer Autenticação:** Sim (Bearer Token)
- **Exemplo de Requisição:**
    - Usando `curl`:
        ```bash
        curl -X GET http://127.0.0.1:5000/cards -H "Authorization: Bearer $TOKEN"
        ```
- **Resposta de Sucesso:**
    ```json
    [
        {
            "id": 1,
            "card_number": "1234567812345678",
            "user_id": 1
        },
        {
            "id": 2,
            "card_number": "8765432187654321",
            "user_id": 1
        }
    ]
    ```
- **Código de Resposta:** `200 OK`

## Executar Testes

Para executar os testes unitários:
```bash
python -m unittest discover -s tests
