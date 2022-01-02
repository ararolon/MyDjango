import pytest
# Tests de los urls de Usuarios
from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve
from Usuarios.views import *

class Test_urls(SimpleTestCase):

    def test_index_usuarios(self):
        url = reverse('index_usuario')
        self.assertEqual(resolve(url).func,index_usuarios)

    def test_verUsuario(self):

        url = reverse('verdetalle',args='0')
        self.assertEqual(resolve(url).func,ver_detalles)

    def test_eliminar_usuario(self):
        url = reverse('eliminaruser',args='0')
        self.assertEqual(resolve(url).func,eliminar_usuario)

    def test_verusuario_error(self):
        #comprueba que tira un error al no asociar con la vista correcta
        url= reverse('verdetalle',args='1')
        self.assertEqual(resolve(url).func,index_usuarios)

    def test_index_eliminar(self):
        url =reverse('indexeliminar')
        self.assertEqual(resolve(url).func,index_eliminarusuario)

    def test_eliminar_usuario_error(self):
        #error al no pasar el tipo de argumento adecuado
        url= reverse('eliminaruser',args=2)
        self.assertEqual(resolve(url).func,eliminar_usuario)
