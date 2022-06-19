from django.urls import path, include
from rest_framework_nested import routers
from news_portal.apps.user.api import views as views_user


router = routers.DefaultRouter(trailing_slash=True)
router.register(r"login", views_user.UserLoginViewSet, basename="user-login")
router.register(r"profile", views_user.UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
