from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def inicio_sesion(request):
    return render(request, 'iniciosesion-index.html')

def register_user(request):
    return render(request, 'registro-usuario.html')