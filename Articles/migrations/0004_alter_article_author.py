# Generated by Django 3.2.7 on 2021-11-11 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
        ('Articles', '0003_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, default='Admin', on_delete=django.db.models.deletion.CASCADE, to='Main.author'),
        ),
    ]
