
from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.test import  Client
from django.urls import reverse
from RolesdeSistema.views import *
from RolesdeSistema.models import RolesdeSistema

class Test_views(TestCase):

    def setUp(self):
        self.client = Client()
        self.usuario = User.objects.create(id='1',username='test',email='email@mail.com')
        self.usuario.set_password('12345')
        self.usuario.save()
        self.grupo = Group.objects.create(name='administrador')
        self.index_roles_sistema_url = reverse('index_rol_sistema')
        self.nuevo_rol_url = reverse('nuevo_rol')
        self.listar_rol_url = reverse('listar_roles')
        self.user = User.objects.create(id ='2',username='test2',password='678910')
        self.grupo2 = Group.objects.create(name='usuarios')


    def tearDown(self):
        self.usuario.delete()
        self.grupo.delete()
        self.user.delete()
        self.grupo2.delete()

    def test_index_roles_sistema(self):
       self.usuario.groups.add(self.grupo)
       self.usuario.save()
       self.client.login(username='test',password='12345')
       response = self.client.get(self.index_roles_sistema_url)
       self.assertTrue(response.status_code, 200)
       self.assertTemplateUsed(response,'RolesdeSistema/index_rol_sistema.html')


    def test_crear_nuevo_rol(self):
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        response = self.client.get(self.nuevo_rol_url)
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,'RolesdeSistema/nuevo_rol.html')

    def test_rol_creado(self):
        #verifica que luego de crear el rol, redirecciona al indice de roles
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        rol = RolesdeSistema.objects.create(
                nombre='rol',
                descripcion='descripcion1'
                )
        rol.save()
        response = self.client.post(rol)
        self.assertTrue(response,self.index_roles_sistema_url)


    def test_crear_nuevo_rol_error(self):
        #verifica que al no iniciar sesion , no se redirecciona al url
        response= self.client.get(self.nuevo_rol_url)
        self.assertNotEqual(response.status_code,200)

    def test_modificar_rol(self):
        #verifica que se usa la plantilla correcta y el url correcto
        rol = RolesdeSistema.objects.create(
            id = '5',
            nombre= 'rol_prueba',
            descripcion= 'alguna_descripcion'
        )
        self.modificar_rol_url = reverse('editar_rol', args= '5')
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        response = self.client.get(self.modificar_rol_url)
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,'RolesdeSistema/Modificar_rol.html')

    def test_rol_modificado(self):
        #cuando el rol esta modificado , redirecciona al indice
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        rol1 = RolesdeSistema.objects.create(
                id='8',
                nombre='rol',
                descripcion='desc'
            )
        rol1.save()
        response = self.client.post(rol1)
        self.assertTrue(response,self.index_roles_sistema_url)


    def test_listar_roles(self):
      #verifica si se usa el url y el template correcto para listar los roles
      self.usuario.groups.add(self.grupo)
      self.usuario.save()
      self.client.login(username='test',password='12345')
      response = self.client.get(self.listar_rol_url)
      self.assertTrue(response.status_code,200)
      self.assertTemplateUsed(response,"RolesdeSistema/Listar_roles_sistema.html")


    def test_listar_roles_error(self):
        #Lanza error porque no se inicia sesion
        response = self.client.get(self.listar_rol_url)
        self.assertEqual(response.status_code,200)

    def test_ver_detalles_rol(self):
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        rol = RolesdeSistema.objects.create(
            id='6',
            nombre='rol2',
            descripcion='alguna_descripcion'
        )
        self.client.login(username='test',password='12345')
        response = self.client.get(reverse('ver_detalles',args='6'))
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,"RolesdeSistema/ver_detalles.html")


    def test_ver_detalles_error(self):
        #si el usuario no es administrador, requiere login
        self.user.groups.add(self.grupo2)
        self.user.save()
        rol = RolesdeSistema.objects.create(
            id='2',
            nombre='rol_sistema',
            descripcion='desc2'
        )
        self.client.login(username='test2',password='678910')
        response =self.client.get(reverse('ver_detalles',args='2'))
        self.assertNotEqual(response.status_code,200)


   # Agregar luego una prueba de cuando el rol este en uso con un proyecto
