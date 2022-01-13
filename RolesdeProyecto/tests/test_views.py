from django.contrib.auth.models import User, Group
from django.test import TestCase, Client
from django.urls import reverse
from RolesdeProyecto.views import *

class Test_views(TestCase):

    def setUp(self):
        self.client = Client()
        self.usuario = User.objects.create(id='1',username='test',email='email@mail.com')
        self.usuario.set_password('12345')
        self.grupo = Group.objects.create(name='administrador')
        self.index_roles_proyecto_url = reverse('index_rol_proyecto')
        self.nuevo_rol_url = reverse('nuevo_rol_proyecto')
        self.listar_roles_url = reverse('listar_roles_proyecto')
        self.user = User.objects.create(id ='2',username='test2')
        self.user.set_password('8910')
        self.grupo2 = Group.objects.create(name='usuarios')


    def tearDown(self):
        self.usuario.delete()
        self.grupo.delete()
        self.user.delete()
        self.grupo2.delete()

    def test_index_roles_proyecto(self):
       self.usuario.groups.add(self.grupo)
       self.usuario.save()
       self.client.login(username='test',password='12345')
       response = self.client.get(self.index_roles_proyecto_url)
       self.assertTrue(response.status_code, 200)
       self.assertTemplateUsed(response,'RolesdeProyecto/index_rol_proyecto.html')


    def test_crear_nuevo_rol(self):
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        response = self.client.get(self.nuevo_rol_url)
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,'RolesdeProyecto/nuevo_rol.html')

    def test_rol_creado(self):
        #verifica que luego de crear el rol, redirecciona al indice de roles
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        rol=  RolesDeProyecto.objects.create(
                nombre='rol',
                descripcion='descripcion1'
                )
        rol.save()
        response = self.client.post(rol)
        self.assertTrue(response,self.index_roles_proyecto_url)

    def test_crear_nuevo_rol_error(self):
        #verifica que al no iniciar sesion , no se redirecciona al url
        response= self.client.get(self.nuevo_rol_url)
        self.assertNotEqual(response.status_code,200)


    def test_modificar_rol(self):
        #verifica que se usa la plantilla correcta y el url correcto
        rol = RolesDeProyecto.objects.create(
            id='5',
            nombre='rol_prueba',
            descripcion='alguna_descripcion'
        )
        self.moficar_rol_url = reverse('editar_rol_proyecto', args= '5')
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test')
        if self.usuario.groups == 'administrador':
            response = self.client.get(self.moficar_rol_url)
            self.assertTrue(response.status_code,200)
            self.assertTemplateUsed(response,'RolesdeProyecto/Modificar_rol.html')

    def test_rol_modificado(self):
        #cuando el rol esta modificado , redirecciona al indice
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        if self.usuario.groups == 'administrador':
            rol1 = RolesDeProyecto.objects.create(
                id='8',
                nombre='rol',
                descripcion='desc'
            )
            rol1.save()
            response = self.client.post(rol1)
            self.assertTrue(response,self.index_roles_proyecto_url)
            self.assertTemplateUsed(response,'RolesdeProyecto/index_rol_proyecto.html')


    def test_listar_roles(self):
      #verifica si se usa el url y el template correcto para listar los roles
      #creamos un rol, para que detecte la existencia de algun rol.
      rol = RolesDeProyecto.objects.create(
            nombre='rol_prueba',
            descripcion= 'descripcion'
      )
      self.usuario.groups.add(self.grupo)
      self.usuario.save()
      self.client.login(username='test',password='12345')
      response = self.client.get(self.listar_roles_url)
      self.assertTrue(response.status_code,200)
      self.assertTemplateUsed(response,"RolesdeProyecto/Listar_roles_proyecto.html")

    def test_no_existe_rol(self):
        #si no existe el rol, usa el template de no existe rol
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        response = self.client.get(self.listar_roles_url)
        self.assertTemplateUsed(response,"RolesdeProyecto/NoexisteRol.html")


    def test_ver_detalles_rol(self):
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        rol = RolesDeProyecto.objects.create(
            id='6',
            nombre='rol2',
            descripcion='alguna_descripcion'
        )
        self.client.login(username='test',password='12345')
        response = self.client.get(reverse('ver_detalles_proyecto',args='6'))
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,"RolesdeProyecto/ver_detalles.html")


    def test_ver_detalles_error(self):
        #si el usuario no es administrador,no ingresar a la vista
        self.user.groups.add(self.grupo2)
        self.user.save()
        rol = RolesDeProyecto.objects.create(
            id='2',
            nombre='rol_proyecto',
            descripcion='desc2'
        )
        self.client.login(username='test2',password='8910')
        response = self.client.get(reverse('ver_detalles_proyecto',args='2'))
        self.assertTrue(response,reverse('home'))


    def test_eliminar_rol(self):
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        rol = RolesDeProyecto.objects.create(
              id = 3,
              nombre='rol5',
              descripcion='desc8'
        )
        self.client.login(username='test',password='12345')
        response =self.client.get(reverse('eliminar_rol_proyecto',args='3'))
        self.assertTrue(response.status_code,200)
        self.assertTemplateUsed(response,'RolesdeProyecto/eliminar_rol.html')


    def test_rol_eliminado(self):
        #cuando el rol es eliminado, tiene que redireccionar a la lista de roles de proyecto
        self.usuario.groups.add(self.grupo)
        self.usuario.save()
        self.client.login(username='test',password='12345')
        rol = RolesDeProyecto.objects.create(
                id ='4',
                nombre='rol',
                descripcion='descripcion3'
        )
        rol.save()
        response = self.client.delete(rol)
        self.assertTrue(response,self.listar_roles_url)


    """
    Agregar luego una prueba de cuando el rol este en uso
    """
