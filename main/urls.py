from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('feedbacks',views.listFeedback, name='feedbacklist'),
    path('formFeedback',views.formFeedback, name='feedbackform'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dataFeedback/',views.api_feedback, name= 'dataFeedback'),
]
