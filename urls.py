from django.urls import path
from .views import listar_autores

urlpatterns = [
    path('autor/', listar_autores),
]