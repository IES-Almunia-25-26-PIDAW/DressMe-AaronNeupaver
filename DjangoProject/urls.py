from django.contrib import admin
from django.urls import path
from inicio.views import home 
from inicio import views
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', home, name='home'),
    path('login/', views.inicio_sesion, name='login'),
    path('register/', views.register_user, name='register'),
]