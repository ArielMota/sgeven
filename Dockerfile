# Utilizando uma imagem base do Python com a versão desejada
FROM python:3.11-slim

# Instalar dependências de compilação do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpcre3 libpcre3-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Diretório de trabalho dentro do contêiner
WORKDIR /core

# Copiar o arquivo de dependências para dentro do contêiner
COPY requirements.txt /core/

# Rodar as migrações antes de iniciar a aplicação
#RUN python manage.py migrate

# Instalar as dependências incluindo o uWSGI
RUN pip install --upgrade pip
RUN pip install uwsgi  # Instalando o uwsgi
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py 
# Copiar o restante do código para dentro do contêiner
COPY . /core/

# Expor a porta que o Django vai rodar
EXPOSE 8101

# Comando para rodar o uWSGI, que servirá a aplicação Django
CMD ["uwsgi", "--socket", "/tmp/sgeven.sock", "--module", "core.wsgi:application"]
