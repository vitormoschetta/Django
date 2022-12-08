from django.urls import path
from app.views import show_players


urlpatterns = [
    path('show_players', show_players, name='show_players'),
]
