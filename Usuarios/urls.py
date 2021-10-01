from django.urls import path, include
from django.views.generic import TemplateView

from Usuarios import views

"""
    Archivo de urls de vistas sobre administracion
    de usuarios del sistema
"""

urlpatterns = [
    path('', views.user_home, name='userhome'),

]