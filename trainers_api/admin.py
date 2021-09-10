from django.contrib import admin
from .models import Treinador,TipoPokemon,Pokemon

# Register your models here.

class Treinadores(admin.ModelAdmin):
    list_display = ("id","nome")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 20
    
   
admin.site.register(Treinador, Treinadores)


class Pokemons(admin.ModelAdmin):
    list_display = ("id","nome","tipo")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 20
    

admin.site.register(Pokemon, Pokemons)


class TiposPokemons(admin.ModelAdmin):
    list_display = ("id","nome")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_per_page = 20
    

admin.site.register(TipoPokemon, TiposPokemons)
