from rest_framework import serializers
from news_portal.apps.news import models as models_news



class SourceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = models_news.Source
        fields = [
            "id",
            "name",
            "source_id",
            "description",
            "url",
            "category",
            "language",
            "country"
        ]


class TopHeadlineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = models_news.TopHeadline
        fields = [
            "id",
            "source",
            "headline_id",
            "name",
            "author",
            "title",
            "description",
            "url",
             "urlToImage",
            "publishedAt",
            "content"
        ]


class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = models_news.Article
        fields = [
            "id",
            "source",
            "author",
            "title",
            "description",
            "url",
            "urlToImage",
            "publishedAt",
            "content",

        ]