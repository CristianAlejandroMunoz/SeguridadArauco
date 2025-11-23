# visitas/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Visita

class VisitaModelTest(TestCase):
    def test_crear_visita(self):
        v = Visita.objects.create(fecha='2025-01-01', supervisor='Juan', zona='Faena 1', estado='pendiente')
        self.assertEqual(str(v), '2025-01-01 - Juan - Faena 1')

class VisitaViewTest(TestCase):
    def setUp(self):
        self.user = None
    def test_lista_sin_login_redirige(self):
        response = self.client.get(reverse('visitas:lista_visitas'))
        self.assertEqual(response.status_code, 302)  # redirect to login
