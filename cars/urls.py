from django.urls import path
from rest_framework.routers import DefaultRouter

from cars.views import CarViewSet


router = DefaultRouter()

router.register('', CarViewSet)

urlpatterns = [
    path('update_attachments/', CarViewSet.as_view({'put': 'update_attachments'})),
    path('delete_attachments/', CarViewSet.as_view({'delete': 'delete_attachments'})),
] + router.urls
