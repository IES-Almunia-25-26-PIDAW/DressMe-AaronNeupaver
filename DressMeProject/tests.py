from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Prenda, OutfitFavorito

class DressMeTests(TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='testpassword123')
        
    def test_homepage_loads(self):
        """Prueba que la página de inicio carga correctamente (código 200)"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        """Prueba que un usuario puede iniciar sesión correctamente"""
        login_success = self.client.login(username='testuser', password='testpassword123')
        self.assertTrue(login_success)
        
    def test_creacion_prenda(self):
        """Prueba que se puede crear un registro de prenda en la base de datos"""
        prenda = Prenda.objects.create(
            usuario=self.user,
            nombre='Camiseta Roja de Prueba',
            categoria='Camiseta',
            # No pasamos imagen real para el test unitario rápido
        )
        self.assertEqual(Prenda.objects.count(), 1)
        self.assertEqual(prenda.nombre, 'Camiseta Roja de Prueba')

    def test_dashboard_protegido(self):
        """Prueba que el dashboard redirige al login si no estás autenticado (Seguridad)"""
        response = self.client.get(reverse('dashboard'))
        # Debería redirigir (código 302) a la página de login
        self.assertEqual(response.status_code, 302)
