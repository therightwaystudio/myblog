from django.shortcuts import render
from django.shortcuts import redirect
from myfirstblog.models import Article
from .forms import ArticleForm
from django.utils import timezone


def about(request):
    return render(request, 'about.html')


def index(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
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