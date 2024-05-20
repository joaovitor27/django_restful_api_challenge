# API Django para Gerenciamento de Usuários, Pedidos e Itens

## Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/joaovitor27/django_restful_api_challenge.git
    cd django_restful_api_challenge
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

4. Crie as migrações e migre o banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Endpoints

### Gerenciamento de Usuários

- **Criar Usuário**: `POST /api/v1/register/`
- **Login**: `POST /api/v1/login/`
- **Perfil do Usuário**: `GET /api/v1/users/`, `PUT /api/v1/users/`, `PATCH /api/v1/users/`

### Gerenciamento de Itens

- **Criar Item**: `POST /api/v1/items/`
- **Listar Itens**: `GET /api/v1/items/`
- **Detalhe do Item**: `GET /api/v1/items/<id>/`, `PUT /api/v1/items/<id>/`, `PATCH /api/v1/items/<id>/`, `DELETE /api/v1/items/<id>/`

### Gerenciamento de Pedidos

- **Criar Pedido**: `POST /api/v1/orders/`
- **Listar Pedidos do Usuário**: `GET /api/v1/orders/user/`
- **Detalhe do Pedido**: `GET /api/v1/orders/<id>/`

## Documentação da API

A documentação completa da API pode ser encontrada em `/swagger/` ou `/redoc/` após iniciar o servidor.

