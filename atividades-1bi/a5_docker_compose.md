# Atividade A5 Docker Compose 

## Parte 1

- Utilizando o Dockerfile criado na atividade anterior
- Crie um arquivo compose.yaml para subir o container do projeto com django
- Faça o build com o comando `docker compose build .`
- Suba o container com o comando `docker compose up`
- Suba no github com o commit "Atividade A5 docker compose parte 1"


## Parte 2

Vamos implementar o banco de dados no docker compose

- Copie o compose.yaml para compose_parte1.yaml
- Crie o serviço de banco de dados no compose.yaml
- Adicione as variáveis de ambiente no compose.yaml
- Adicione o volume para o banco de dados
- Adicione o link entre o serviço do django e o banco de dados (dependência)
- Configure o banco de dados no settings.py
- Inclusa a dependência do psycopg2 no Dockerfile
- Faça o build com o comando `docker compose build .`
- Suba o container com o comando `docker compose up`
- Suba no github com o commit "Atividade A5 docker compose parte 2"
