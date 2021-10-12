from django.urls import path, include
from django.views.generic import TemplateView

from Usuarios import views

"""
    Archivo de urls de vistas sobre administracion
    de usuarios del sistema
"""

urlpatterns = [
    path('',views.index_usuarios,name='index_usuario'),
    path('VerUsuario/<int:id>',views.ver_detalles,name='verdetalle'),
    path('Eliminar_usuario/<int:id>',views.eliminar_usuario, name='eliminaruser'),
    path('Index_eliminar',views.index_eliminarusuario,name='indexeliminar'),
]