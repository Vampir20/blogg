from django.shortcuts import render

# Create your views here.
def news_page(request):
    return render(request, "News/news.html")