from django.shortcuts import render
from .models import Article
from django.db.models import Q
# Create your views here.

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Article.objects.filter(Q(title__icontains=q)| Q(tegs_icontains=q))
    else:
        articles = Article.objects.all().order_by('-id')
        q=None

    return render(request, 'home.html', {"articles":articles, 'q':q})