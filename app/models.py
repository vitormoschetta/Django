from django.db import models

# Create your models here.
# Use Django ORM to create a model for the database
class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')  # verbose_name é o nome que aparece no painel de administração para o campo

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')    

    def __str__(self):
        return self.name


class PlayerTeam(models.Model):
    player = models.ManyToManyField(Player, verbose_name='Jogador')
    team = models.ManyToManyField(Team, verbose_name='Time')
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return [player.name for player in self.player.all()].__str__()

