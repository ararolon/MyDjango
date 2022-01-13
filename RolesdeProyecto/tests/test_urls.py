from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve
from RolesdeProyecto.views import *

class Test_urls(SimpleTestCase):

    def test_index_rol_proyecto(self):
        url = reverse('index_rol_proyecto')
        self.assertEqual(resolve(url).func,vista_principal)

    def test_crear_nuevo_rol(self):
        url = reverse('nuevo_rol_proyecto')
        self.assertEqual(resolve(url).func,crear_nuevo_rol)

    def test_nuevo_rol_error(self):
        #verifica que el url no envia a la vista principal
        url = reverse('nuevo_rol_proyecto')
        self.assertNotEqual(resolve(url).func,vista_principal)

    def test_modificar_rol(self):
        url = reverse('editar_rol_proyecto',args='0')
        self.assertEqual(resolve(url).func,modificar_rol)

    def test_eliminar_rol(self):
        url = reverse('eliminar_rol_proyecto',args='0')
        self.assertEqual(resolve(url).func,eliminar_rol)

    def test_listar_roles(self):
         url = reverse('listar_roles_proyecto')
         self.assertEqual(resolve(url).func,listar_roles)

    def test_detalles_rol(self):
        url = reverse('ver_detalles_proyecto',args='0')
        self.assertEqual(resolve(url).func,detalles_rol)