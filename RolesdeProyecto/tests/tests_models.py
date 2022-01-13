from django.contrib.auth.models import Permission
from django.test import TestCase
from RolesdeProyecto.models import RolesDeProyecto


class Test_models(TestCase):

    def setUp(self):
        self.rol1= RolesDeProyecto.objects.create(
            nombre = 'rol1',
            descripcion = 'decs',
        )
        self.rol1.save()
        #agrega todos los permisos que inicien con pp
        for permisos in Permission.objects.filter(codename__startswith='pp'):
            self.rol1.permisos.add(permisos)

        self.rol1.save()


    def test_fields_rol_correctos(self):
      #se prueba si los campos del rol creado se han guardado correctamente
      self.assertTrue(self.rol1.nombre,'rol1')
      self.assertTrue(self.rol1.nombre,'desc')
      self.assertTrue(self.rol1.permisos.exists())






