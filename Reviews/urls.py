from django.urls import path
from Reviews.views import reviews_page
urlpatterns = [
path("", reviews_page)
]