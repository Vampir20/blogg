# Generated by Django 3.2.7 on 2021-11-18 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_categories'),
        ('Articles', '0007_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.author'),
        ),
    ]
