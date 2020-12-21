# from selenium import webdriver

from django.test import LiveServerTestCase, TestCase, tag, Client
from django.urls import resolve, reverse
from django.http import HttpRequest, response
from .models import *
from .views import signUp, login_view, logout_view
from .forms import SignUpForm, LoginForm

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
       
        response = Client().get('/formFeedback')
        self.assertTemplateUsed(response,"main/feedbackForm.html")

    def test_main_penggunaan_templateIndex(self):
        response = Client().get('/')
        self.assertTemplateUsed(response,"main/home.html")
    
    #login page
    def test_does_login_page_exist(self):
        response = Client().get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_check_function_used_by_login(self):
        found = resolve('/login/')
        self.assertEqual(found.func, login_view)
    
    def test_does_login_views_show_correct_template(self):
        response = Client().get('/login/')
        self.assertTemplateUsed(response, 'main/login.html')
    
    #sign up page

    def test_does_signup_page_exist(self):
        response = Client().get('/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_check_function_used_by_signup(self):
        found = resolve('/signup/')
        self.assertEqual(found.func, signUp)
    
    def test_does_signup_views_show_correct_template(self):
        response = Client().get('/signup/')
        self.assertTemplateUsed(response, 'main/signup.html')
    
    #sign out test

    def test_does_sign_out_work(self):
        response = Client().get('/logout/')
        self.assertEqual(response.status_code, 302)
    
    def test_check_function_used_by_logout(self):
        found = resolve('/logout/')
        self.assertEqual(found.func, logout_view)
    
    #test login form
    
    def test_forms_login_invalid(self):
        form_login = LoginForm(data={
            "username": "a",
            "password": ""
        })
        self.assertFalse(form_login.is_valid())
    
    #test sign up form

    def test_forms_signup_valid(self):
        form_reg = SignUpForm(data={
            "username": "sipewe",
            "email": "sipewe@example.com",
            'password1': 'test12345',
            'password2': 'test12345',
        })
        self.assertTrue(form_reg.is_valid())
    
    def test_forms_signup_invalid(self):
        form_reg = SignUpForm(data={
            "username": "",
            "email": "sipewe@example.com",
            'password1': 'test12345',
            'password2': 'test123',
        })
        self.assertFalse(form_reg.is_valid())
    
class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login = reverse("main:login")
        self.signup = reverse("main:signup")
    
    def test_POST_login_valid(self):
        response = self.client.post(self.login,
                                    {
                                        'username': 'sipewe',
                                        'password ': "test12345"
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_POST_login_invalid(self):
        response = self.client.post(self.login,
                                    {
                                        'username': '',
                                        'password ': ""
                                    }, follow=True)
        self.assertTemplateUsed(response, 'main/login.html')
    
    def test_POST_signup_valid(self):
        response = self.client.post(self.signup,
                                    {
                                        "username": "sipewe",
                                        "email": "sipewe@example.com",
                                        'password1': 'test12345',
                                        'password2': 'test12345',
                                    }, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_POST_signup_invalid(self):
        response = self.client.post(self.signup,
                                    {
                                        "username": "sipewe",
                                        "email": "sipewe@example.com",
                                        'password1': 'test12345',
                                        'password2': 'test123',
                                    }, follow=True)
        self.assertTemplateUsed(response, 'main/signup.html')

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
