from django.contrib import admin

from app.models import Player, PlayerTeam, Team

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(PlayerTeam)