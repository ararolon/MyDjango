#prueba de views
import pytest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from SSO.views import *

class Test_views(TestCase):

    def setUp(self):
      self.client = Client()
      self.home_url = reverse('home')
      self.configuracion_inicial_url = reverse('confinicial')
      self.logout_url = reverse('logout')
      self.configurarion_url = reverse('confinicial')
      #creamos un usuario de prueba
      self.usuario = User.objects.create(username= 'test',first_name='a', last_name='b', email='email@email.com')
      self.usuario.save()
      self.user = User.objects.create(username='test2',first_name='b', last_name='c', email='email2@email.com')
      self.user.save()
      # crea el grupo de administrador
      group_name = "administrador"
      self.group = Group(name=group_name)
      self.group.save()
      #crea el grupo de usuarios
      group_name2 = "usuarios"
      self.grupo = Group(name=group_name2)
      self.grupo.save()
      self.usuario2 = User.objects.create(username='test5',first_name='d', last_name='c', email='email3@email.com')

    def tearDown(self):
        self.user.delete()
        self.usuario.delete()
        self.group.delete()
        self.grupo.delete()


    def test_home_administrador(self):
      #agregamos al usuario al grupo de administrador
      self.user.groups.add(self.group)
      self.user.save()
      self.client.login(username='test')
      if self.user.groups == 'administrador' :
        response = self.client.get("/home")
        #verifica que el path sea /home
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,'Home.html')

    def test_home_usuarios(self):
        # agregamos al usuario al grupo de usuarios
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test2')
        if self.usuario.groups == 'usuarios':
            response = self.client.get("/home")
            #verifica que el path sea /home
            self.assertTrue(response.status_code,200)
            self.assertTemplateUsed(response,'Home_usuario.html')

    def test_error_login(self):
     #que no redireccione a /home si no ha iniciado sesion ningun usuario
      response = self.client.get('/home')
      self.assertTemplateUsed(response,'Home.html')


    def test_logout_view(self):
      response = self.client.get(self.logout_url)
      #pregunta si la vista redirecciona a la siguiente direccion
      self.assertTrue(response,redirect('/accounts/logout/'))

    def test_configuracion_inicial(self):
        response = self.client.get(self.configuracion_inicial_url)
        #redirecciona a home
        self.assertTrue(response,self.home_url)

    #faltan los tests de los render de los templates