
from django.contrib import admin
from django.urls import path 


from . import views

urlpatterns = [
    path('', views.default_path, name='default_path'),
    path('register_users/', views.register_users, name='register_users'),
    path('register/post', views.register_post, name='register'),

    
]