from django.test import TestCase, Client, LiveServerTestCase
from django.urls import resolve, reverse
from .views import *
from .models import *
from .forms import *
import time
from main.views import signUp
from django.contrib.auth import login
from django.contrib.auth.models import User


# Create your tests here!
class qna_testPath(TestCase):
    def test_path_qna(self):
        c = Client()
        c.login(username='fred', password='secret')
        response = c.get('/qna/',{},True)
        self.assertEquals(response.status_code,200)
    def test_path_balas(self):
        new_model = pertanyaan.objects.create(penanya ='sabeb', pertanyaan='sabeb')
        response = Client().get('/balas/1/',{},True)
        self.assertEquals(response.status_code,200)
    def test_path_dataqna(self):
        response = Client().get('/dataqna',{},True)
        self.assertEquals(response.status_code,200)
    def test_path_datakomen(self):
        response = Client().get('/datakomen',{},True)
        self.assertEquals(response.status_code,200)

class qna_testInput(TestCase):
    def test_input_qna(self):
        response = Client().get('/qna/')
        html = response.content.decode('utf-8')
        self.assertIn('LETS DISCUSS ABOUT COVID',html)
        self.assertIn('Back',html)
        self.assertIn('Post',html)
    def test_input_balas(self):
        new_model = pertanyaan.objects.create(penanya ='Gilang', pertanyaan='Apa itu Covidify')
        komen = komentar.objects.create(pengomentar='Cey', komen="Ini adalah ..", tanya=new_model)
        response = Client().get('/balas/1/',{},True)
        html = response.content.decode('utf-8')
        self.assertIn('LETS DISCUSS ABOUT COVID',html)
        self.assertIn('Gilang',html)
        self.assertIn('Apa itu Covidify',html)
        self.assertIn('View all 1 comments',html)
    
class qna_testFunction(TestCase):
    def test_url_using_func(self):
        found = resolve('/qna/')
        self.assertEqual(found.func, forum)
    def test_url_using_func2(self):
        new_model = pertanyaan.objects.create(penanya ='Gilang', pertanyaan='Apa itu Covidify')
        found = resolve('/balas/1/')
        self.assertEqual(found.func, balas)
    def test_url_using_func3(self):
        found = resolve('/dataqna/')
        self.assertEqual(found.func, api_pertanyaan)
    def test_url_using_func4(self):
        found = resolve('/datakomen/')
        self.assertEqual(found.func, api_komen)

class qna_testModel(TestCase):
    def test_create_pertanyaan(self):
        new_model = pertanyaan.objects.create(penanya ='Gilang', pertanyaan='Apa itu Covidify')
        counting_new_model = pertanyaan.objects.all().count()
        self.assertEqual(counting_new_model,1)
    def test_create_komentar(self):
        pertanyaan1 = pertanyaan.objects.create(penanya ='Gilang', pertanyaan='Apa itu Covidify')
        new_model = komentar.objects.create(pengomentar ='Catur', komen='Covidify itu blabla', tanya=pertanyaan1)
        counting_new_model = komentar.objects.all().count()
        self.assertEqual(counting_new_model,1)

class qna_testTemplate(TestCase):
    def test_form_template_used1(self):
        response = Client().get('/qna/')
        self.assertTemplateUsed(response, 'forum.html')
    def test_form_template_used3(self):
        pertanyaan1 = pertanyaan.objects.create(penanya ='Gilang', pertanyaan='Apa itu Covidify')
        response = Client().get('/balas/1/',{},True)
        self.assertTemplateUsed(response, 'forum-pertanyaan.html')

class qna_testForm(TestCase):
    def test_post_formPertanyaan(self):
        c = Client()
        c.login(username='gilangcy', password='gilang2001')
        response =c.post('/qna/',{
				'pertanyaan':'Apa ini?'

			})
        html = response.content.decode('utf-8')
    def test_post_formkomen(self):
        c = Client()
        c.login(username='gilangcy', password='gilang2001')
        pertanyaan1 = pertanyaan.objects.create(penanya ='Gilang', pertanyaan='Apa itu Covidify')
        response =c.post('/balas/1/',{'komen':'Apa ini?'})
        html = response.content.decode('utf-8')

    


