from django.contrib import admin
from news_portal.apps.user import models as models_user

model_list = [models_user.User]

admin.site.register(*model_list)
