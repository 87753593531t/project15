from django.urls import path
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet


router = DefaultRouter()

router.register('', ProductViewSet)

urlpatterns = [
    path('update_attachments/', ProductViewSet.as_view({'put': 'update_attachments'})),
    path('delete_attachments/',ProductViewSet.as_view({'delete': 'delete_attachments'})),
] + router.urls
