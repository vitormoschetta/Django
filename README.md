# Django

### Cria virtual env
```
virtualenv --python=python3.10 venv
```


### Ativa virtual env
```
source venv/bin/activate
```


### Instala pipenv
```
pip3 install pipenv
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
python manage.py startapp app
```


### Cria modelos/classes no `models.py`
```
from django.db import models

# Create your models here.
# Use Django ORM to create a model for the database
class Player(models.Model):
    name = models.CharField(max_length=50)    

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)    

    def __str__(self):
        return self.name


class PlayerTeam(models.Model):
    player = models.ManyToManyField(Player)
    team = models.ManyToManyField(Team)
    name = models.CharField(max_length=50)

    def __str__(self):
        return [player.name for player in self.player.all()].__str__()
```


### Cria migrations
```
python manage.py makemigrations
```

### Aplica migrations
```
python manage.py migrate
```


### Cria painel administrativo para os modelos criados

Ir no arquivo `admin.py` e adicionar o seguinte código
```
from django.contrib import admin

from app.models import Player, PlayerTeam, Team

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(PlayerTeam)
``` 

Com apenas isso, já é possível acessar o painel administrativo com o CRUD completo para o modelo "Player", "Team" e "PlayerTeam".


### Traduz o painel administrativo

Ir no arquivo `settings.py` e adicionar o seguinte código
```
LANGUAGE_CODE = 'pt-br'
```

### Adicionar páginas / templates

Criar um arquivo `app/urls.py` e adicionar o seguinte código
```
from django.urls import path
from app.views import show_players

urlpatterns = [
    path('show_players', show_players, name='show_players'),
]
```

Ir no arquivo `app/views.py` e adicionar o seguinte código
```
def show_players(request):
    players = Player.objects.all()
    return render(request, 'app/players.html', {'players': players})
```

Criar o arquivo `app/templates/app/players.html` e adicionar o seguinte código
```
<h1>Listar Jogadores</h1>

<ol>
{% for player in players %}
<li>{{ player.name }}</li>
{% endfor %}
</ol>
```

Ir no arquivo `cartola_fc/urls.py` e adicionar o seguinte código
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
```

Acessar a página `http://localhost:8001/show_players`


### Criar backup do banco de dados
```s
python manage.py dumpdata --format=json --indent=4 > db.json
```
<br>


## Referências

https://www.youtube.com/watch?v=NC6aUo5rxco