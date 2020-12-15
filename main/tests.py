# from django.test import LiveServerTestCase, TestCase, tag
# from django.urls import reverse
# from selenium import webdriver


from django.test import LiveServerTestCase, TestCase, tag
from django.urls import reverse
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest, response
from main.models import *
import main.views
# from selenium import webdriver
class DetailTest(TestCase):
    def test_input_feedback(self):
        feedback = Feedback.objects.create(nama="arya",feedbackUser="Kreen sekali")
        count = Feedback.objects.all().count()
        self.assertEqual(count,1)

    def test_main_url_is_exist (self) :
        response = Client().get('/feedbacks')
        self.assertEqual(response.status_code, 200)
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_penggunaan_templateFeedback(self):
        feedback = Feedback.objects.create(nama="arya",feedbackUser="Kreen sekali")
       
        response = Client().get('/feedbacks')
        self.assertTemplateUsed(response,"main/feedbackList.html")

    def test_main_penggunaan_templateIndex(self):
        response = Client().get('/')
        self.assertTemplateUsed(response,"main/home.html")


# @tag('functional')
# class FunctionalTestCase(LiveServerTestCase):
#     """Base class for functional test cases with selenium."""

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         # Change to another webdriver if desired (and update CI accordingly).
#         options = webdriver.chrome.options.Options()
#         # These options are needed for CI with Chromium.
#         options.headless = True  # Disable GUI.
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         cls.selenium = webdriver.Chrome(options=options)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()


# class MainTestCase(TestCase):
#     def test_root_url_status_200(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         # You can also use path names instead of explicit paths.
#         response = self.client.get(reverse('main:home'))
#         self.assertEqual(response.status_code, 200)


# class MainFunctionalTestCase(FunctionalTestCase):
#     def test_root_url_exists(self):
#         self.selenium.get(f'{self.live_server_url}/')
#         html = self.selenium.find_element_by_tag_name('html')
#         self.assertNotIn('not found', html.text.lower())
#         self.assertNotIn('error', html.text.lower())
