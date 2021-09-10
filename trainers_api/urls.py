from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('trainer',views.TreinadorViewSet)
router.register('pokemon',views.PokemonViewSet)



urlpatterns = [
    path("list/",include(router.urls)),
]