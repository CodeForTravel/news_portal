# Generated by Django 3.2.10 on 2022-06-19 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('category', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TopHeadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('urlToImage', models.URLField()),
                ('publishedAt', models.DateTimeField()),
                ('content', models.CharField(max_length=255)),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.source')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('urlToImage', models.URLField()),
                ('publishedAt', models.DateTimeField()),
                ('content', models.CharField(max_length=255)),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.source')),
            ],
        ),
    ]
