# desafio_hyperativa
Desafio Oportunidade Hyperativa
# Credit Card API

## Setup

1. Clone o repositório:
    ```bash
    git clone <repo_url>
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `.env`:
    ```plaintext
    SECRET_KEY=your_secret_key
    DATABASE_URL=sqlite:///app.db
    JWT_SECRET_KEY=your_jwt_secret_key
    ```

5. Inicialize o banco de dados:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Execute a aplicação:
    ```bash
    python run.py
    ```

## Endpoints

- `POST /register`: Registrar um novo usuário.
- `POST /login`: Fazer login e obter token JWT.
- `POST /add_card`: Adicionar um número de cartão.
- `GET /check_card/<card_number>`: Verificar se um número de cartão existe.
- `POST /add_cards_from_file`: Adicionar números de cartão a partir de um arquivo TXT.

## Testes

Para executar os testes:
```bash
python -m unittest discover -s tests
