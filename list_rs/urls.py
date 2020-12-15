from django.urls import path
from .views import tambahRS, listRS
app_name = 'list_rs'
urlpatterns = [
    path('tambahRS/',tambahRS, name='tambahRS'),
    path('listRS/',listRS,name = 'listRS'),
    
]
