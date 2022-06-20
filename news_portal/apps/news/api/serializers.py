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
    source_detail = serializers.SerializerMethodField()
    class Meta:
        model = models_news.TopHeadline
        fields = [
            "id",
            "source",
            "source_detail",
            "author",
            "title",
            "description",
            "url",
             "urlToImage",
            "publishedAt",
            "content"
        ]

    def get_source_detail(self, obj):
        if obj.source:
            return SourceSerializer(obj.source).data
        return None



