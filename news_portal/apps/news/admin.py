from django.contrib import admin
from news_portal.apps.news import models as models_news


admin.site.register(models_news.Source)
admin.site.register(models_news.TopHeadline)
admin.site.register(models_news.Article)