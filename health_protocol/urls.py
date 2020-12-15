from django.urls import path
from .views import index, alternatives, upvote, downvote

app_name = 'health_protocol'

urlpatterns = [
    path('health_protocol/', index, name='healthProtocol'),
    path('alternatives/', alternatives, name='alternatives'),
    path('upvote/<int:pk>', upvote, name='upvote'),
    path('downvote/<int:pk>', downvote, name='downvote'),
]