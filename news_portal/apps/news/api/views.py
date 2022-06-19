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


    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            country_of_news = user.country_of_news
            country_of_news = [s.lower() for s in country_of_news]
            qs = self.queryset.filter(source__country__in=country_of_news, source__in=user.news_sources.all())
            return qs
        else:
            return self.queryset