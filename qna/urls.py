from django.urls import path

from . import views

app_name = 'qna'

urlpatterns = [
     path('qna/',views.forum,name='forum'),
     path('balas/<int:komen_id>/' ,views.balas, name='balas'),
     path('dataqna/', views.api_pertanyaan, name = 'dataqna'),
     path('datakomen/', views.api_komen, name = 'datakomen'),
]