from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('membros/', views.members, name='members'),
    path('artigos/', views.articles, name='articles'),
    path('projetos/', views.projects, name='projects'),
    path('contato/', views.contact, name='contact'),
]
