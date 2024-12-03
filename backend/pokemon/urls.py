from django.urls import path
from . import views

urlpatterns = [
    path('pokemons/<pags>', views.GetAllPokemons.as_view()),
    path('pokemon/<pokeid>', views.GetPokemonById.as_view()),
]
