from django.shortcuts import render, redirect, get_object_or_404
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Prenda, OutfitFavorito
from django.utils import timezone
from datetime import timedelta

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
        
    prendas = Prenda.objects.filter(usuario=request.user)
    total_prendas = prendas.count()
    # Asumimos una "capacidad máxima" visual de 100 prendas para la barra de progreso
    porcentaje_armario = min((total_prendas / 100) * 100, 100) if total_prendas > 0 else 0
    ultimas_prendas = prendas.order_by('-fecha_creacion')[:4]
    
    una_semana_atras = timezone.now() - timedelta(days=7)
    outfits_guardados = OutfitFavorito.objects.filter(usuario=request.user).count()
    outfits_esta_semana = OutfitFavorito.objects.filter(usuario=request.user, fecha_creacion__gte=una_semana_atras).count()
    
    context = {
        'total_prendas': total_prendas,
        'porcentaje_armario': porcentaje_armario,
        'ultimas_prendas': ultimas_prendas,
        'outfits_guardados': outfits_guardados,
        'outfits_esta_semana': outfits_esta_semana,
    }
    return render(request, 'dashboard.html', context)

def armario(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')
        
        if nombre and categoria and imagen:
            Prenda.objects.create(
                usuario=request.user,
                nombre=nombre,
                categoria=categoria,
                imagen=imagen
            )
            messages.success(request, 'Prenda añadida correctamente.')
            return redirect(request.META.get('HTTP_REFERER', 'armario'))
            
    prendas = Prenda.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'armario.html', {'prendas': prendas})

def eliminar_prenda(request, prenda_id):
    if not request.user.is_authenticated:
        return redirect('login')
        
    prenda = get_object_or_404(Prenda, id=prenda_id, usuario=request.user)
    
    if request.method == 'POST':
        prenda.delete()
        messages.success(request, 'Prenda eliminada correctamente.')
        
    return redirect(request.META.get('HTTP_REFERER', 'armario'))

def ia_outfits(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    context = {}
    if request.method == 'POST':
        prendas = Prenda.objects.filter(usuario=request.user)
        camisetas = list(prendas.filter(categoria='Camiseta'))
        pantalones = list(prendas.filter(categoria='Pantalón'))
        zapatos = list(prendas.filter(categoria='Zapato'))
        accesorios = list(prendas.filter(categoria='Accesorio'))
        
        if not camisetas or not pantalones or not zapatos:
            context['error'] = 'Necesitas tener subida al menos 1 Camiseta, 1 Pantalón y 1 Zapato en tu armario para generar un outfit básico.'
        else:
            outfit = [
                random.choice(camisetas),
                random.choice(pantalones),
                random.choice(zapatos)
            ]
            
            # Añadir un accesorio aleatorio (70% de probabilidad para mayor variedad)
            if accesorios and random.random() < 0.7:
                outfit.append(random.choice(accesorios))
                
            context['outfit'] = outfit
            
    return render(request, 'ia_outfits.html', context)

def guardar_outfit(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == 'POST':
        prenda_ids = request.POST.getlist('prendas')
        if prenda_ids:
            nuevo_outfit = OutfitFavorito.objects.create(usuario=request.user)
            # Fetch prendas ensuring they belong to user
            prendas = Prenda.objects.filter(id__in=prenda_ids, usuario=request.user)
            nuevo_outfit.prendas.set(prendas)
            messages.success(request, '¡Outfit guardado en favoritos!')
            return redirect('favoritos')
            
    return redirect('ia_outfits')

def favoritos(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    outfits = OutfitFavorito.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'favoritos.html', {'outfits': outfits})

def eliminar_outfit(request, outfit_id):
    if not request.user.is_authenticated:
        return redirect('login')
        
    outfit = get_object_or_404(OutfitFavorito, id=outfit_id, usuario=request.user)
    
    if request.method == 'POST':
        outfit.delete()
        messages.success(request, 'Outfit eliminado de favoritos.')
        
    return redirect('favoritos')