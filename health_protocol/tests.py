from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import *
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.models import Pengguna

# Create your tests here.
class TestModel(TestCase):
    def test_if_alternatives_model_exist(self):
        Alternatives.objects.create(text="Banyak doa", upvotes=0, downvotes=0)
        hitung_jumlah_data = Alternatives.objects.all().count()
        self.assertEquals(hitung_jumlah_data, 1)

class TestForm(TestCase):
    def test_if_alternatives_form_is_valid(self):
        alternativesForm = AlternativesForm(data={"text":"Banyak doa"})
        self.assertTrue(alternativesForm.is_valid())

    def test_if_alternatives_form_is_invalid(self):
        alternativesForm = AlternativesForm(data={})
        self.assertFalse(alternativesForm.is_valid())

class TestURL(TestCase):
    def test_if_health_protocol_url_exists(self):
        response = Client().get('/health_protocol/')
        self.assertEquals(response.status_code, 200)

    def test_if_alternatives_url_exists(self):
        response = Client().get('/alternatives/')
        self.assertEquals(response.status_code, 200)

class TestFunc(TestCase):
    def test_health_protocol_url_using_func(self):
        found = resolve('/health_protocol/')
        self.assertEqual(found.func, index)

    def test_alternatives_url_using_func(self):
        found = resolve('/alternatives/')
        self.assertEqual(found.func, alternatives)

class TestView(TestCase):
    
    def test_if_health_protocol_template_exists_on_the_page(self):
        response = Client().get('/health_protocol/')
        self.assertTemplateUsed(response, 'health_protocol/index.html')

    def test_if_alternatives_template_exists_on_the_page(self):
        response = Client().get('/alternatives/')
        self.assertTemplateUsed(response, 'health_protocol/alternatives.html')
