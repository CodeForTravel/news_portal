from django.urls import path, include
from rest_framework_nested import routers
from news_portal.apps.news.api import views as views_news


router = routers.DefaultRouter(trailing_slash=True)
router.register(r"sources", views_news.SourceViewSet, basename="sources")
router.register(r"top-headlines", views_news.TopHeadlineViewSet, basename="top-headlines")

urlpatterns = [
    path("", include(router.urls)),
]
