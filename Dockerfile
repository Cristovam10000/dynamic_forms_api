FROM python:3.10-slim

WORKDIR /app

# Instalar dependências de SO (para psycopg2)
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia arquivos de configuração
COPY .env.example .env
COPY requirements.txt .

# Instala deps Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
