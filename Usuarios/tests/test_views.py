#prueba de views
import pytest
from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse
from Usuarios.views import *

class Test_views(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_usuario_url = reverse('index_usuario')
        self.verusuario_url = reverse('verdetalle',args='2')
        self.eliminaruser_url = reverse('eliminaruser',args='1')
        self.index_eliminar_usuario_url = reverse('indexeliminar')
        self.grupo1= Group.objects.create(name='administrador')
        self.user = User.objects.create(id='1', username='test1', email='email2@mail.com')
        self.user.set_password('8910')
        self.user.save()
        self.user.groups.add(self.grupo1)
        self.user.save()
        self.usuario = User.objects.create(id='2',username='test',email='email1@mail.com')
        self.usuario.set_password('1234')
        self.usuario.save()

    def tearDown(self):
      self.grupo1.delete()
      self.user.delete()
      self.usuario.delete()

    def test_index_usuarios(self):
       #la vista de indice de usuarios del sistema se muestra solo al administrador
       self.client.login(username='test1',password='8910')
       response = self.client.get(self.index_usuario_url)
       self.assertTrue(response.status_code,200)
       self.assertTemplateUsed(response,'Usuarios/index_usuarios.html')

    def test_ver_detalles(self):
       self.client.login(username='test1',password='8910')
       response = self.client.get(self.verusuario_url)
       self.assertTrue(response.status_code,200)
       self.assertTemplateUsed(response,'Usuarios/VerDetalles.html')

    def test_eliminar_usuario(self):
        self.client.login(username='test1',password='8910')
        response = self.client.get(self.eliminaruser_url)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'Usuarios/eliminar.html')

    def test_index_eliminar_usuario(self):
        #prueba si la vista usa el template y el url correcto
        self.client.login(username='test1',password='8910')
        response = self.client.get(self.index_eliminar_usuario_url)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response,'Usuarios/index_eliminar.html')

    def test_eliminar_usuario_redirect(self):
        #prueba que una vez eliminado el usuario , redirecciona a indexeliminar
        self.client.login(username='test1',password='8910')
        response = self.client.post(self.usuario)
        self.assertTrue(response,reverse('indexeliminar'))

