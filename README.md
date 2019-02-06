# mluiza_bckend

## Desafio Magalu Backend 
(https://99prod.s3.amazonaws.com/uploads/document/file/65/7f3e828797d345d5d7abfd151f505538.pdf)

### - Criar uma API Rest para gerenciamento de salas de reunião.

#### Infos:
 - Utilizado Python, Django, Djangorestframework, Docker(requerimento para o projeto)
 - Dados persistidos em banco de dados local relacional sqlite3
 - Repositorio https://github.com/cawan1/mluiza_bckend
 
 *Desafio completo.*
 
 Passos para execução do Projeto:
  
  1. ```docker pull cawanporto/django-rest-framework```
  2. ```git clone https://github.com/cawan1/mluiza_bckend.git```
  3. ```cd mluiza_bckend/meeting_room```
  4. ```docker run -d --name="cp_magalu" -p 80:80 -v `pwd`:/app cawanporto/django-rest-framework runserver 0.0.0.0:80```
  5. ```docker exec -it cp_magalu python manage.py makemigrations```
  6. ```docker exec -it cp_magalu python manage.py migrate```
  7. ```curl http://localhost/api/``` - Possivel Acessar API via Browser
  8. ```docker exec -it cp_magalu python manage.py test booking```
  
  
  #### Listar, Criar, Editar, Excluir *Salas*:
  
  GET /api/salas/
  
  POST /api/salas/
  
  PUT /api/salas/{id}
  
  DELETE /api/salas/{id}
  
  ```
  json {
    "nome": "Sala01" 
  }
  ```
  
  ##### Exemplo: 
  curl -H "Content-Type: application/json" -X POST -d '{"nome" : "Sala01"}' http://localhost/api/salas
    
  #### Listar, Criar, Editar, Excluir *Agendamentos*:
  
  GET /api/agendamentos/
  
  POST /api/agendamentos/
  
  PUT /api/agendamentos/{id}
  
  DELETE /api/agendamentos/{id}
  
  ```
  json  {
    "titulo": "Reuniao_1",
    "sala": 1,
    "inicio_reserva": "2019-03-02T01:00:00",
    "fim_reserva": "2019-03-02T02:00:00"
   }
   ```
   
   ##### Exemplo: 
  curl -H "Content-Type: application/json" -X POST -d \
   ' { \
    "titulo": "Reuniao_1", \
    "sala": 1, \
    "inicio_reserva": "2019-03-02T01:00:00", \
    "fim_reserva": "2019-03-02T02:00:00" \
      }' \
   http://localhost/api/agendamentos
