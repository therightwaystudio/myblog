from django.shortcuts import render
from myfirstblog.models import Article


def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def contact(request):
    return render(request, 'contact.html')


def show_article(request,article_id):
    article = Article.objects.get(id=article_id)
    return render(request,'article.html',{'article': article})