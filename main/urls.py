from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('feedbacks',views.listFeedback, name='feedbacklist'),
    path('formFeedback',views.formFeedback, name='feedbackform')
]
