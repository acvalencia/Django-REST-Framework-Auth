from email.policy import default
from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

TYPE_USER = (
    (True, 'INTERNO'),
    (False, 'EXTERNO')
)

ROL_ACCESS = (
    (False, 'OR'),
    (True, '')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    # custom fields for user
    rol_acceso   = models.BooleanField('Rol de acceso', choices=ROL_ACCESS, default=False , blank=True, null=True)
    tipo_usuario = models.BooleanField('Tipo de usuario', choices=TYPE_USER, default=False, blank=True, null=True)
    nombre       = models.CharField('Nombres', max_length=100, blank=True, null=True)
    apellido     = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    cedula       = models.CharField('Cedula', max_length=255, blank=True, null=True, unique=True)
    telefono     = models.CharField('Teléfono', max_length=255, blank=True, null=True)
    activo       = models.BooleanField('Activo', default=True, null=True)

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kwargs):
        if created:
            UserProfile.objects.get_or_create(user=instance)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.user.email
