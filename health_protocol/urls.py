from django.urls import path
from .views import index, alternatives, upvote

app_name = 'health_protocol'

urlpatterns = [
    path('health_protocol/', index, name='healthProtocol'),
    path('alternatives/', alternatives, name='alternatives'),
    path('upvote/', upvote, name='upvote'),
]
