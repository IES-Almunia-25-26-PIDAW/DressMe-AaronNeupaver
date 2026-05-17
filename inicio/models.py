from django.db import models
from django.contrib.auth.models import User

class Prenda(models.Model):
    CATEGORIAS = [
        ('Camiseta', 'Camiseta'),
        ('Pantalón', 'Pantalón'),
        ('Zapato', 'Zapato'),
        ('Accesorio', 'Accesorio')
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    imagen = models.ImageField(upload_to='prendas/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class OutfitFavorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    prendas = models.ManyToManyField(Prenda)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Outfit de {self.usuario.username} - {self.fecha_creacion.strftime('%d/%m/%Y')}"

# Señal para borrar la imagen física cuando se borra la prenda
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

@receiver(post_delete, sender=Prenda)
def eliminar_imagen_al_borrar_prenda(sender, instance, **kwargs):
    """Borra el archivo físico de la imagen cuando se elimina el registro de la base de datos."""
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)
