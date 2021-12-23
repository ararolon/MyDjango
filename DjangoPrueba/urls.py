
from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #path del sso de google
    path('', include('SSO.urls')),
    path('usuarios/',include('Usuarios.urls')),
    path('RolesdeProyecto/',include('RolesdeProyecto.urls')),
    path('RolesdeSistema/',include('RolesdeSistema.urls')),

]
