from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def inicio_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        contrasena = request.POST.get('password')
        
        user = authenticate(request, username=usuario, password=contrasena)
        
        if user is not None:
            if user.email == email:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'El correo electrónico no coincide con este usuario.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            
    return render(request, 'iniciosesion-index.html')

def register_user(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        contrasena = request.POST.get('password')
        
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Ese nombre de usuario ya existe.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Ese correo electrónico ya está registrado.')
        else:
            user = User.objects.create_user(username=usuario, email=email, password=contrasena)
            messages.success(request, '¡Registro completado con éxito! Ahora puedes iniciar sesión.')
            return redirect('login')
            
    return render(request, 'registro-usuario.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html')