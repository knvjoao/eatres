from django.shortcuts import render
from .models import Usuario

def listadeusuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listadeusuarios.html', {'usuarios': usuarios})