from django.shortcuts import render
from Articles.models import Article
# Create your views here.

def main_page(request):
    first_article = Article.objects.get(id=1)
    return render(request, 'Main/main_page.html', locals())