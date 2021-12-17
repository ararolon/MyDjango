from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView

from RolesdeProyecto import views

urlpatterns = [
              path('crear_rol_p/',views.crear_nuevo_rol,name='nuevo_rol'),
              path('roles_proyecto/',views.vista_principal,name='index_rol_proyecto'),
              path('modificar_rol_p/<str:pk>',views.modificar_rol,name='editar_rol'),
              path("eliminar_rol_p/<str:pk>",views.eliminar_rol,name='eliminar_rol'),
              path("lista_roles_p/",views.listar_roles,name='listar_roles'),
              path("Detalles_rol_p/<str:pk>",views.detalles_rol,name='ver_detalles'),
]
