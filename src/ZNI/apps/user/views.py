from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.user.serialzers import UserTokenSerializer
from datetime import datetime

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.user)
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                # Si el usuario no tiene asignado un token lo crea y se lo asigna
                if created:
                    return Response({'token': token.key,
                                     'user': user_serializer.data,
                                     'message': 'Inicio de sesión exitoso.'}, status = status.HTTP_201_CREATED)
                else:
                    #Si el usuario tiene una sesión activa y abre otra sesión, se elimina la anterior
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    # Si el usuario ya tiene creado un token, lo borra y genera un nuevo token
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({'token': token.key,'user': user_serializer.data,'message': 'Inicio de sesión exitoso.'}, status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED) 
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)
        
        return Response({'mensaje':'Hola desde response'}, status = status.HTTP_200_OK)