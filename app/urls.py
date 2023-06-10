from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:id>/', views.detailsArticle, name='articleDetails'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>', views.projectDetails, name='projectDetails'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test')
]
