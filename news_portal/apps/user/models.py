from calendar import TUESDAY
import pytz
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models.fields.json import JSONField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from news_portal.apps.news import models as models_news


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=255,
        unique=True,
        help_text=_(
            "Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    name = models.CharField(_("Name"), blank=True, max_length=255)   

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})

    # user newfeed settings
    news_sources = models.ManyToManyField(models_news.Source, blank=True)
    country_of_news = JSONField("Country of news",null=True, blank=True)
    news_keywords = JSONField("News keywords",null=True, blank=True)




