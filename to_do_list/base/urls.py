from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
]