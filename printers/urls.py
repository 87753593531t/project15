from django.urls import path
from rest_framework.routers import DefaultRouter

from printers.views import PrinterViewSet


router = DefaultRouter()

router.register('', PrinterViewSet)

urlpatterns = [
    path('update_attachments/', PrinterViewSet.as_view({'put': 'update_attachments'})),
    path('delete_attachments/', PrinterViewSet.as_view({'delete': 'delete_attachments'})),
] + router.urls