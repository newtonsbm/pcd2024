# Comandos Docker 

- CLI CheatSheet: https://docs.docker.com/get-started/docker_cheatsheet.pdf 

## Geral

- `docker pull namespace/nome_imagem:nome_tag` : download da imagem a partir do DockerHub
- `docker image ls` : listar imagens Docker localmente armazenadas
- `docker run namespace/nome_image:nome_tag`: executa um container a partir de uma imagem
- `docker run -p porta_host:porta_container namespace/imagem:tag` : executa um container realizando um mapemaento de portas entre host e container (guest)
- `docker run -p porta_host:porta_container -v path/host:past/container/guest namespace/imagem:tag` : executa um container com mapeamento de portas e mapeamento de volume
