from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Librería del token
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'), # <-- Ruta de prueba que se accede solo si se envía el token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- Link para obtener el token
    path('register',views.RegisterUserAPIView.as_view()),
]