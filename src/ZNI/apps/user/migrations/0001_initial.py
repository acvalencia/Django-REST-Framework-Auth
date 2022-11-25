# Generated by Django 4.1.1 on 2022-10-13 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_acceso', models.BooleanField(blank=True, choices=[(False, 'OR'), (True, '')], default=False, null=True, verbose_name='Rol de acceso')),
                ('tipo_usuario', models.BooleanField(blank=True, choices=[(True, 'INTERNO'), (False, 'EXTERNO')], default=False, null=True, verbose_name='Tipo de usuario')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('cedula', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Cedula')),
                ('telefono', models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono')),
                ('activo', models.BooleanField(default=True, null=True, verbose_name='Activo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
