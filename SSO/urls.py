


"""
    urls de la app de SSO de Google , vistas de paginas principales
    login y logout del proyecto
"""

from django.urls import path, include
from django.views.generic import TemplateView

from SSO import views

urlpatterns = [
    path('',views.configuraciones_iniciales,name='confinicial'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]