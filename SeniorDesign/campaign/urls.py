from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('projects/', views.projects, name='projects'),
    path('create-project/', views.create_project, name='create_project'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
]