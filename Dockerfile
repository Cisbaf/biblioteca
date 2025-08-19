FROM python:3.12-slim

# Define diretório de trabalho na imagem final
WORKDIR /app

# Instala dependências de runtime necessárias para mysqlclient funcionar
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev pkg-config default-libmysqlclient-dev poppler-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY /src .

RUN pip install -r requirements.txt

# Copia entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expõe a porta usada pela aplicação
EXPOSE 8000

# Define entrypoint
ENTRYPOINT ["/entrypoint.sh"]
