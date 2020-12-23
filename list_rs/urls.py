from django.urls import path
from .views import tambahRS, listRS, api_rs
app_name = 'list_rs'
urlpatterns = [
    path('tambahRS/',tambahRS, name='tambahRS'),
    path('listRS/',listRS,name = 'listRS'),
    path('data/', api_rs, name = 'data'),
]
