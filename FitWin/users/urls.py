from django.urls import path
from . import views

urlpatterns = [
    path('trainers', views.handler_trainers, name='main'),
    path('clients', views.handler_clients, name='main'),
    path('client_details', views.handler_client_details, name='main'),


]