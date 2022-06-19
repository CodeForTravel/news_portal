from rest_framework import serializers
from django.contrib.auth import get_user_model
from news_portal.apps.user import models as models_user
from news_portal.core.api.serializers import DynamicFieldsModelSerializer
from django.utils.translation import ugettext_lazy as _


User = get_user_model()

class UserProfileSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = models_user.User
        fields = [
            "id",
            "username",
            "name",
            "email"
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User