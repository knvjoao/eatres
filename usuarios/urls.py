from django.urls import path
from .views import listadeusuarios

urlpatterns = [
    path('usuarios/', listadeusuarios, name='listadeusuarios'),
]