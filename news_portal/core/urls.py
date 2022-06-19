from django.urls import path
from news_portal.core import views as views_core

app_name = "core"

urlpatterns = [
    path("", views_core.IndexView.as_view(), name="home"),
]


# urls for non login, password reset
auth_template_url_paths = [
    ["login/", "login"],
    ["account/password_reset/", "password-reset"],
    ["account/password_reset/done/", "password-reset-done"],
    ["account/reset/done/", "password-reset-complete"],
    ["account/reset/<str:token>/confirm/", "password-reset-confirm"],
]
for path__ in auth_template_url_paths:
    urlpatterns.append(
        path(path__[0], views_core.IndexView.as_view(), name=path__[1]))


# urls for logged in user
sysadmin_dashboard_url_paths = [
    # first index is path, second index is name
    ["profile/", "profile"],
]
for path__ in auth_template_url_paths:
    urlpatterns.append(
        path(path__[0], views_core.AuthenticatedIndexView.as_view(), name=path__[1]))