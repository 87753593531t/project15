from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, LoginViewSet


router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view())
] + router.urls
