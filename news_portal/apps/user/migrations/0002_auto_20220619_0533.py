# Generated by Django 3.2.10 on 2022-06-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country_of_news',
            field=models.JSONField(blank=True, null=True, verbose_name='Country of news'),
        ),
        migrations.AddField(
            model_name='user',
            name='news_keywords',
            field=models.JSONField(blank=True, null=True, verbose_name='News keywords'),
        ),
        migrations.AddField(
            model_name='user',
            name='news_sources',
            field=models.ManyToManyField(to='news.Source'),
        ),
    ]
