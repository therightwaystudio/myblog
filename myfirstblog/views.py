from django.shortcuts import render
from django.shortcuts import redirect
from myfirstblog.models import Article
from .forms import ArticleForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate


def about(request):
    return render(request, 'about.html')


def index(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.user = request.user;
            post.published_date = datetime.datetime.now()

            post.save()
            return redirect('/')
    else:
        form = ArticleForm()
    return render(request, 'index.html', {'articles': articles,'form': form})


def contact(request):
    return render(request, 'contact.html')


def show_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article.html', {'article': article})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
