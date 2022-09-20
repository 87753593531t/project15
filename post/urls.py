from django.urls import path
from rest_framework.routers import DefaultRouter

from post.views import PostViewSet


router = DefaultRouter()

router.register('', PostViewSet)

urlpatterns = [
    path('posts/', PostViewSet.as_view({'put': 'posts'})),
    path('delete_attachments/',PostViewSet.as_view({'delete': 'delete_attachments'})),
] + router.urls