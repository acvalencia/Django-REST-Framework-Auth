from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserRegisterSerializer

class UserRegisterAPI(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
