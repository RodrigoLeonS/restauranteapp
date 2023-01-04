from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny  # <-- se importan los permisos
from rest_framework import generics

#serializer
from .serializers import RegisterSerializer



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- Se indica que tiene que estar autenticado para ingresar a esta vista

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer