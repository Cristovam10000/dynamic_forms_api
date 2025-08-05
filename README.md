# Dynamic Forms API

API de formulários dinâmicos construída com FastAPI e SQLAlchemy.
API de formulários dinâmicos construída com **FastAPI** e **SQLAlchemy**, utilizando **PostgreSQL** como banco de dados.


## Recursos
- CRUD completo de formulários e perguntas.
- Listagem de perguntas com filtros, ordenação e paginação.
- Documentação interativa em `/docs`.
- Endpoint de verificação de saúde em `/health`.

## Pré‑requisitos
- Python 3.11+
- PostgreSQL
- PostgreSQL 15+
- Opcional: Docker e Docker Compose

## Configuração
1. Copie o arquivo `.env.example` para `.env` e ajuste as variáveis de acordo com o seu ambiente:
## Configuração do Ambiente
1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone <url-do-repo>
   cd dynamic_forms_api
   ```
2. Copie o arquivo `.env.example` para `.env` e ajuste as variáveis conforme seu ambiente:
   ```bash
   cp .env.example .env
   ```
2. Crie e ative um ambiente virtual (opcional):
   Variáveis disponíveis:
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`
   - `POSTGRES_DB`
   - `POSTGRES_HOST`
   - `POSTGRES_PORT`

### Executando localmente
1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Garanta que o PostgreSQL esteja em execução e execute as migrações:
   ```bash
   alembic upgrade head
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   uvicorn app.main:app --reload
   ```
5. A API estará disponível em `http://localhost:8000`.

## Executando
Inicie o servidor local com:
```bash
uvicorn app.main:app --reload
```
A documentação automática estará disponível em `http://localhost:8000/docs`.
### Executando com Docker
1. Certifique‑se de que Docker e Docker Compose estejam instalados.
2. Suba os serviços:
   ```bash
   docker-compose up --build
   ```
3. Aplique as migrações (apenas na primeira vez ou após mudanças no modelo):
   ```bash
   docker-compose run --rm web alembic upgrade head
   ```
4. Acesse `http://localhost:8000` para utilizar a API.

## Principais Endpoints
- **Formulários**
  - `POST /formularios`
  - `GET /formularios`
  - `GET /formularios/{form_id}`
  - `PUT /formularios/{form_id}`
  - `DELETE /formularios/{form_id}`
- **Perguntas**
  - `POST /formularios/{form_id}/perguntas`
  - `GET /formularios/{form_id}/perguntas`
  - `GET /formularios/{form_id}/perguntas/{question_id}`
  - `PUT /formularios/{form_id}/perguntas/{question_id}`
  - `DELETE /formularios/{form_id}/perguntas/{question_id}`

### Parâmetros da listagem de perguntas
`GET /formularios/{form_id}/perguntas`

## Rotas principais
- **Formulários**: CRUD completo em `/formularios`
- **Perguntas**: CRUD completo em `/formularios/{form_id}/perguntas`
| Parâmetro       | Descrição                                    |
|-----------------|----------------------------------------------|
| `tipo`          | Filtra pelo tipo de pergunta (texto, número…) |
| `obrigatoria`   | Filtra por obrigatoriedade (`true`/`false`)   |
| `ordering`      | Campo para ordenação                          |
| `skip`          | Quantidade de itens a ignorar                 |
| `limit`         | Quantidade máxima de itens retornados         |

## Saúde
Verifique o status do serviço em:
## Saúde do Serviço
Verifique o status do serviço:
```bash
curl http://localhost:8000/health
```