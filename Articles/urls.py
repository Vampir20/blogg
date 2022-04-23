from django.urls import path
from Articles.views import articles_page, detail_article, detail_category

urlpatterns = [
    path("", articles_page, name="articles"),
    path("detail/<int:pk>", detail_article, name="detail_article"),
    path("category/<int:pk>", detail_category, name="detail_category")

]
