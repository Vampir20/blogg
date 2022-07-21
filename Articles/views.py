from django.shortcuts import render, redirect
from Articles.models import Article
from Main.models import Categories


def articles_page(request):
    all_slides = Article.objects.filter(on_slider=True)
    all_articles = Article.objects.all()
    all_categories = categories_counter()
    return render(request, "Article/articles.html", locals())


def detail_article(request, pk):
    item = Article.objects.get(id=pk)
    last_five_news = Article.objects.all().order_by('-date')[:5]
    return render(request, "Article/article-deatail.html", locals())


def detail_category(request, pk):
    all_articles = Article.objects.filter(category_id=pk)
    category_name = Categories.objects.get(id=pk)
    return render(request, "Article/detail-category.html", locals())


def categories_counter():
    categories = {}
    all_categories = Categories.objects.all()
    for category_name in all_categories:
        count_article = len(Article.objects.filter(category=category_name))
        if count_article > 0:
            categories.update({
                category_name: count_article
            })
    return categories


def view404(request, exception):
    return redirect("articles")
