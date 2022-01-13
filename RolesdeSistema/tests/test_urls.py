from django.test import SimpleTestCase
from django.urls import resolve, reverse

from RolesdeSistema.views import *


class TestUrls(SimpleTestCase):

   #Test de los urls de roles de sistema

   def test_index_rol_sistema(self):
      url = reverse('index_rol_sistema')
      self.assertEqual(resolve(url).func, vista_principal)

   def test_crear_nuevo_rol(self):
      url = reverse('nuevo_rol')
      self.assertEqual(resolve(url).func, crear_nuevo_rol)

   def test_modificar_rol(self):
      url = reverse('editar_rol', args='0')
      self.assertEqual(resolve(url).func, modificar_rol)

   def test_listar_roles(self):
      url = reverse('listar_roles')
      self.assertEqual(resolve(url).func, listar_roles)

   def test_detalles_rol(self):
      url = reverse('ver_detalles', args='0')
      self.assertEqual(resolve(url).func, detalles_rol)
