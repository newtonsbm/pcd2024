# Atividade A12 - Rabiit

- Veja o exemplo em aula e implemente dois novos serviços ligados ao mecanismo de mensageria do rabbit
    - 1 serviço de envio de SMS que segue o padrão do whatsapp e de mailing
        - Deve consumir da mesma fila que os anteriores e simular o processo de envio de SMS
    - 1 serviço de geração de nota fiscal
        - Necessário criar o Consumer que via gerar a nota fiscal, olhar o padrão dos outros consumer porém nesse caso será uma fila simples 
        - Alterar o Producer (serviço cafepao) para gerar esse novo evento (gerar nota fiscal) que será consumido pelo Consumer definido anteriormente
