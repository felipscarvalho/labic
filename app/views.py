from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def members(request):
    return render(request, 'members.html')


def articles(request):
    return render(request, 'articles.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')
