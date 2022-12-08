from django.shortcuts import render

from app.models import Player

# Create your views here.
# Views = Controllers

def show_players(request):
    players = Player.objects.all()
    return render(request, 'app/players.html', {'players': players})