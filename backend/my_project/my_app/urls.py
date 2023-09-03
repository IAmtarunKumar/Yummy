# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    path('data/', views.data, name='data'),
    path('community/show/', views.list_communities, name='showCommunity'),
    path('com/', views.create_community, name='postCommunity'),



    # path('recipe/', views.showRecipe, name='showRecipe'),
    # path('addRecipe/', views.addRecipe, name='addRecipe'),
]
