from django.db import models

# Create your models here.


    
class Treinador(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    idade = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.nome


class TipoPokemon(models.Model):
    
    nome = models.CharField(max_length=50, blank=False, unique=True)
    def __str__(self):
        return self.nome
    
    
class Pokemon(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    tipo = models.ForeignKey(TipoPokemon, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
