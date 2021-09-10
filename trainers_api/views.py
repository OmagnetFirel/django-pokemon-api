from django.shortcuts import render
from rest_framework import  viewsets, generics
from .models import  Treinador,TipoPokemon,Pokemon
from .serializers import TreinadorSerializer,TipoSerializer,PokemonSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TreinadorViewSet(viewsets.ModelViewSet):
    '''Exibe todos os Treinadores(as)'''
    queryset = Treinador.objects.all()
    serializer_class = TreinadorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class PokemonViewSet(viewsets.ModelViewSet):
    '''Exibe todos os Pokemons(as)'''
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TipoViewSet(viewsets.ModelViewSet):
    '''Exibe todos os Tipos(as)'''
    queryset = TipoPokemon.objects.all()
    serializer_class = TipoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
