from django.shortcuts import render
from .models import Articles, Projects, ExtendUser

# Create your views here.


def home(request):
    return render(request, 'home.html')


def members(request):
    participants = ExtendUser.objects.all()
    voluntarios = participants.filter(user_level=1)
    bolsistas = participants.filter(user_level=2)
    orientadores = participants.filter(user_level=3)

    return render(request, 'members.html', {'voluntario': voluntarios, 'bolsista': bolsistas, 'orientador': orientadores})


def articles(request):
    articles = Articles.objects.select_related(
        'author').all().filter(post_status=1).order_by('id').reverse()

    return render(request, 'articles.html', {'articles': articles})


def detailsArticle(request, id):
    article = Articles.objects.select_related(
        'author').filter(post_status=1).get(pk=id)

    return render(request, 'articleDetails.html', {'article': article})


def projects(request):
    projects = Projects.objects.select_related(
        'author').all().filter(project_status=1).order_by('id').reverse()

    return render(request, 'projects.html', {'projects': projects})


def projectDetails(request, id):
    project = Projects.objects.select_related(
        'author').filter(project_status=1).get(pk=id)

    project_id = Projects.objects.get(pk=id)

    articles = Articles.objects.all().filter(
        project=project_id).order_by('id').reverse()
    print(articles, project_id)

    return render(request, 'projectDetails.html', {'project': project, 'articles': articles})


def contact(request):
    return render(request, 'contact.html')


def test(request):
    articles = Articles.objects.all()
    return render(request, 'test.html', {'post': articles})
