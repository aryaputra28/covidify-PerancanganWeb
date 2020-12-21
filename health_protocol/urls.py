from django.urls import path
from .views import index, alternatives, alternativesPreference

app_name = 'health_protocol'

urlpatterns = [
    path('health_protocol/', index, name='healthProtocol'),
    path('alternatives/', alternatives, name='alternatives'),
    path('alternatives/<str:alt_id>/preference/<str:userpreference>', alternativesPreference, name='preference'),
]
