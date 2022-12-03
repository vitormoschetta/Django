# Django

### Cria virtual env
```
virtualenv --python=python3.8 venv
```


### Ativa virtual env
```
source venv/bin/activate
```


### Instala Django
```
pipenv install django
```


### Cria projeto
```
django-admin startproject <NOME_PROJETO>
cd <NOME_PROJETO>
```


### Inicializa banco de dados
```
python manage.py migrate
```


### Cria superuser
```
python manage.py createsuperuser
```
Digite o nome de usuário, email e senha


### Inicia servidor
```
python manage.py runserver
```
Se a porta 8000 estiver ocupada, use o comando abaixo
```
python manage.py runserver 127.0.0.1:<PORTA>
```


### Efetua login no admin
```
http://127.0.0.1:8000/admin
```


### Cria app
```
python manage.py startapp <NOME_APP>
cd <NOME_APP>
```


### Cria classe no `models.py`
```
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50)
    initial_price = models.FloatField()

    def __str__(self):
        return self.name
```


### Cria migrations
```
python manage.py makemigrations
```


### Aplica migrations
```
python manage.py migrate
```


### Cria painel administrativo para novo modelo
Ir no arquivo `admin.py` e adicionar o seguinte código
```
from django.contrib import admin

from app.models import Player

# Register your models here.
admin.site.register(Player)
```
Com apenas isso, já é possível acessar o painel administrativo com o CRUD completo para o modelo "Player".

