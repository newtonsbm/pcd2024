# A2 - Virtualização 

- Instalar VirtualBox
- Instalar Vagrant
- No repositório de atividades individual, criar uma nova pasta chamada a2_virtualizacao
- Entrar na pasta pelo terminal
- Iniciar o projeto Vagrant com os comandos

`vagrant init generic/alpine318` 

- Configurar a porta  descomentando a linha: 
`config.vm.network "forwarded_port", guest: 8000, host: 8080`

- Iniciar vagrant
`vagrant up`

- Acessar a maquina virtual via ssh com
`vagrant ssh`

- Uma vez no container, instale o python e djagno com os comandos

`sudo apk add python3`
`sudo apk add py3-pip`

- Instalar djagno e inicar projeto
`pip install django`
`python3 -m django start_project teste`

- Entrar na pasta e iniciar o servidor
`cd teste`
`python manage.py run_server 0.0.0.0:8000`


## Plus

- Utilize o provisionamento para instalar python automaticamente 
- Tente outro box e instale uma ferramenta diferente
- Suba os testes em um outro Vagrantfile