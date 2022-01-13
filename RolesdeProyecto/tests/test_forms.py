from django.test import TestCase
from RolesdeProyecto.forms import *

class Test_forms(TestCase):

    def setUp(self):
        self.form2 =RolesProyectoForms(data={})


    def test_form_invalido(self):
        self.assertFalse(self.form2.is_valid())

    def test_form_contiene_errores(self):
        self.assertEqual(len(self.form2.errors),2)


