from django.urls import path
from apps.users.api.api import UserAPiView

urlpatterns = [
    path('usuario/', UserAPiView.as_view(), name = 'usuario_api')
]