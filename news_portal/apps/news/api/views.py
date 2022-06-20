import logging
from wsgiref.util import request_uri
from django.urls import reverse
from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from news_portal.apps.news import models as models_news
from news_portal.apps.news.api import serializers as serializers_news
from news_portal.core.api import pagination as pagination_global
from news_portal.apps.news.api import filters as filters_news

logger = logging.getLogger(__name__)


class SourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models_news.Source.objects.all()
    serializer_class = serializers_news.SourceSerializer
    pagination_class = pagination_global.GlobalPagination


class TopHeadlineViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = models_news.TopHeadline.objects.all()
    serializer_class = serializers_news.TopHeadlineSerializer
    pagination_class = pagination_global.GlobalPagination
    filter_backends = [
        filters_news.TopHeadlineFilterBackend,
    ]


    