from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import UserProfile
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('rol_acceso', 'tipo_usuario', 'nombre', 'apellido', 'cedula', 'telefono', 'is_activo',)

class UserSerializer(UserDetailsSerializer):

    profile = UserProfileSerializer(source="userprofile")

    class Meta(UserDetailsSerializer.Meta):
        model = get_user_model()
        fields = UserDetailsSerializer.Meta.fields + ('profile',)

    def update(self, instance, validated_data):
        userprofile_serializer = self.fields['profile']
        userprofile_instance = instance.userprofile
        userprofile_data = validated_data.pop('userprofile', {})
        userprofile_serializer.update(userprofile_instance, userprofile_data)
        instance = super().update(instance, validated_data)
        return instance

class CustomRegisterSerializer(RegisterSerializer):

    rol_acceso   = serializers.BooleanField(default=False)
    tipo_usuario = serializers.BooleanField(default=False)
    nombre       = serializers.CharField(max_length=255)
    apellido     = serializers.CharField(max_length=255)
    cedula       = serializers.CharField(max_length=255)
    telefono     = serializers.CharField(max_length=255)
    activo    = serializers.BooleanField(default=False)

    class Meta:
        fields = UserDetailsSerializer.Meta.fields + ('rol_acceso','tipo_usuario','nombre','apellido','cedula','telefono','is_activo')

    def save(self, request):
        user = super().save(request)
        user.userprofile.rol_acceso   = self.data.get('rol_acceso')
        user.userprofile.tipo_usuario = self.data.get('tipo_usuario')
        user.userprofile.nombre       = self.data.get('nombre')
        user.userprofile.apellido     = self.data.get('apellido')
        user.userprofile.cedula       = self.data.get('cedula')
        user.userprofile.telefono     = self.data.get('telefono')
        user.userprofile.activo       = self.data.get('activo')
        user.userprofile.save()
        user.save()
        return user
