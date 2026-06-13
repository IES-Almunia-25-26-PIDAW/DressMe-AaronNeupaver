from django.contrib import admin
from django.urls import path
from .views import home 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', home, name='home'),
    path('login/', views.inicio_sesion, name='login'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('armario/', views.armario, name='armario'),
    path('armario/eliminar/<int:prenda_id>/', views.eliminar_prenda, name='eliminar_prenda'),
    path('ia-outfits/', views.ia_outfits, name='ia_outfits'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('ia-outfits/guardar/', views.guardar_outfit, name='guardar_outfit'),
    path('favoritos/eliminar/<int:outfit_id>/', views.eliminar_outfit, name='eliminar_outfit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
