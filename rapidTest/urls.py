from django.urls import path
from . import views

app_name = 'rapidTest'

urlpatterns = [
    path('rapidTest/', views.rapidTest, name='rapid'),
    path('formRapid/', views.form_Rapid, name='form'),
]