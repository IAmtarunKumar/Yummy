# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.task_list, name='task_list'),
    path('register/', views.userRegister, name='register'),
    path('login/',views.login , name='login'),
    path('recipe/',views.showRecipe , name='showRecipe'),
    path('addRecipe/',views.addRecipe , name='addRecipe')


    # path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    # path('login/',views.login , name='login')
]
