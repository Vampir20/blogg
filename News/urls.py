from django.urls import path
from News.views import news_page
#отресовка на пустой путь


urlpatterns = [
    path("", news_page, name='news')
]