from rest_framework import serializers
from news_portal.apps.news import models as models_news
from news_portal.core.api.serializers import DynamicFieldsModelSerializer



class SourceSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = models_news.Source
        fields = [
            "id",
            "name",
            "source_id"
            "description"
            "url"
            "category"
            "language"
            "country"
        ]