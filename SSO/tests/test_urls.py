#Tests de las vistas de SS0
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from SSO.views import configuraciones_iniciales


class Test_SSO_urls(SimpleTestCase):


  def Test_configurariones_iniciales(self):
        url = reverse('confinicial')
        print = resolve(url)


