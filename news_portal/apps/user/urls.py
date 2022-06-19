from django.urls import path
from news_portal.apps.user import views as views_user

app_name = "user"

urlpatterns = [
    path("profile/", views_user.UserProfileView.as_view(), name="profile"),
]
