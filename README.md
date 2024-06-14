# Prova2-M10

# Aplicação

Foi criado o logs da aplicação na qual todar as rotas tem um logger do tipo Warning, esses logs são registrados no /logs/app/log mais os históricos.
Foi criado um Docker compose, que quando executado utilizando o 'docker compose up', levanta toda a aplicação (App (com log) e Gateway)
Foi dockerizado a aplicação
Foi criado um arquivo JSON com as requisições do Insominia com os testes de  todas as rotas
Foi criado um Gateway utilizando NGINX  

# Ambiente virtual

Não cheguei a utilizar um ambiente virtual nessa prova, logo fica apenas os comando para iniciar um:
python3 -m venv venv
source venv/bin/activate