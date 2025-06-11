# Backend da Aplicação E-Serviços

Este repositório contém o código do backend da aplicação E-Serviços, desenvolvida com Django e Django REST Framework. Ele gerencia dados de usuários e serviços, oferecendo APIs para cadastro, autenticação, busca e listagem.

## Funcionalidades Principais

* **Autenticação de Usuários:**
    * Cadastro de novos usuários com e-mail, nome de usuário, endereço, contato e nome da empresa.
    * Login de usuários utilizando **e-mail e senha** (e-mail definido como `USERNAME_FIELD`).
    * Logout de usuários.
    * Validação de unicidade para e-mail e nome de usuário, com mensagens de erro customizadas.
    * Validação de confirmação de senha no cadastro.
    * Senhas são armazenadas de forma segura (hashed).
* **Gestão de Serviços:**
    * Cadastro de serviços associados a um usuário (criador/proprietário).
    * Serviços incluem título, descrição, valor e uma imagem.
    * Listagem de todos os serviços.
    * Funcionalidade de busca de serviços por título ou descrição (insensível a maiúsculas/minúsculas).
* **Estrutura de API RESTful:**
    * Endpoints API dedicados para operações de usuário e serviço.
    * Utiliza Serializers do Django REST Framework para fácil serialização/desserialização de dados.
    * Suporte a upload de imagens via `ImageField` (com tratamento para armazenamento).
* **Armazenamento de Dados:**
    * Configurado para usar um banco de dados PostgreSQL (como NeonDB) em produção.
    * Usa SQLite para desenvolvimento local.

## Tecnologias Utilizadas

* **Django:** Framework web principal.
* **Django REST Framework (DRF):** Para construção de APIs RESTful.
* **Python:** Linguagem de programação.
* **Pillow:** Para processamento de imagens (necessário para `ImageField`).

## Configuração do Ambiente Local

Para colocar o backend em funcionamento na sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd E-Services
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    Recomenda-se usar a versão Python 3.10.x.
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Caso `requirements.txt` não exista ou esteja desatualizado, você pode instalar as principais dependências manualmente: `pip install Django djangorestframework Pillow` e depois gerar o arquivo com `pip freeze > requirements.txt`)*.

4.  **Configuração do Banco de Dados:**
    No arquivo `my_project/settings.py` (ou o nome do seu arquivo de settings principal), a configuração padrão usará SQLite para desenvolvimento. Você pode definir a variável de ambiente `DATABASE_URL` se quiser usar um banco de dados externo localmente.

5.  **Aplique as Migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Crie um Superusuário (para acesso ao Admin):**
    ```bash
    python manage.py createsuperuser
    # O comando pedirá o email (seu USERNAME_FIELD) e a senha.
    ```

7.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```
    O backend estará acessível em `http://127.0.0.1:8000/`.

## Endpoints da API

A API está acessível sob o prefixo `/api/`.

* **Usuários:**
    * `GET /api/users/`: Lista todos os users.
    * `POST /api/users/add/`: Cadastro de novo usuário.
    * `DELETE /api/users/<pk>/`: Exclusão de usuário.
* **Serviços:**
    * `GET /api/services//`: Lista todos os serviços.
    * `GET /api/services/search/?q=termo`: Busca serviços por título ou descrição.
    * `POST /api/services/add/`: Cadastro de novo serviço.
