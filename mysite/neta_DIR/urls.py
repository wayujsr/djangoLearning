from django.urls import path
from . import views

urlpatterns = [
    path('', views.neta_list, name='neta_list'),
]