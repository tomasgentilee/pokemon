from django.shortcuts import render
from rest_framework.views import APIView
import json
import urllib.request
from rest_framework.response import Response

class GetPokemonById(APIView):
    def get(self, request, pokeid, *args, **kwargs):
        url = urllib.request.Request(f"https://pokeapi.co/api/v2/pokemon/{pokeid}")
        url.add_header("User-Agent", "pokemon")
        source = urllib.request.urlopen(url).read()
        pokemon = json.loads(source)
        print(pokemon)
        return Response({"data": f"{pokemon}"})


class GetAllPokemons(APIView):
    def get(self, request, pags, *args, **kwargs):
        
        url = urllib.request.Request(f"https://pokeapi.co/api/v2/pokemon?limit=50&offset={pags}")
        url.add_header("User-Agent", "pokemon")
        source = urllib.request.urlopen(url).read()
        pokemons_data = json.loads(source)
        print(pokemons_data['results'])
        return Response(pokemons_data['results'])