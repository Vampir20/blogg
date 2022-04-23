from django.db import models

from Main.models import Author, Categories, Type


class Article (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1, blank=True)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='media/images/articles')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=8128)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=1, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1, blank=True)
    on_slider = models.BooleanField(default=False)