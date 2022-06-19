import logging
from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from news_portal.apps.user import models as models_user
from news_portal.apps.user.api import serializers as serializers_user
from django.contrib.auth import get_user_model
from django.urls import reverse

from django.contrib.auth import login
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)

User = get_user_model()


class UserProfileViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated]
    queryset = models_user.User.objects.all()
    serializer_class = serializers_user.UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(models_user.User, pk=kwargs["pk"])
        serializer = serializers_user.UserProfileSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        user = get_object_or_404(models_user.User, pk=kwargs["pk"])
        serializer = serializers_user.UserProfileSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            kwargs["partial"] = True
            return self.update(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["POST"], url_path="change-password")
    def change_password(self, request, *args, **kwargs):
        user = request.user
        serializer = serializers_user.ChangePasswordSerializer(
            data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.validated_data.get("old_password")):
                return Response(
                    {"old_password": "Wrong password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], url_path="user-info")
    def get_user_info(self, request):
        user = request.user
        serializer = serializers_user.UserProfileSerializer(user)
        return Response(serializer.data)


class UserLoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {"errors": {"__all__": "Please enter both username and password"}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                data = {"detail": "Success"}
                redirect_url = reverse("core:home")
                data["redirect_url"] = redirect_url

                return Response(
                    data,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"detail": "Invalid password!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception:
            return Response(
                {"detail": "Invalid username!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
