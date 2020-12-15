from django.urls import path

from . import views

app_name = 'qna'

urlpatterns = [
     path('qna/',views.forum,name='forum'),
     path('lihatPertanyaan/',views.lihatPertanyaan,name='lihatPertanyaan'),
     path('balas/<int:komen_id>/' ,views.balas, name='balas'),
]