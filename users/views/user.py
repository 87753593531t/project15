from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import CustomUser
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
