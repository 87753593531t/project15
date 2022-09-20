from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from post.models import Post
from post.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from post.permissions import PostOwnerOrReadOnly

class PostViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Post.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = PostSerializer

    def get_serializer_class(self):
        serializer_class = PostSerializer

        if self.action == 'create':
            serializer_class = PostCreateSerializer
        elif self.action == 'update':
            serializer_class = PostUpdateSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = PostSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)
    def get_object(self):
        uuid = self.kwargs['pk']
        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404
    def get_posts(self):
        author = self.request.user

        try:
            instance = Post.objects.filter(authro=author)
            return instance
        except:
            raise Http404
    def list(self, request, *args, **kwargs):
        # instance = self.get_posts()
        serializer = self.get_serializer(self.queryset.all(), many=True)
        return Response(serializer.data)

    def get_permissions(self):

        permission_classes = [AllowAny, ]

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated, ]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes.append(PostOwnerOrReadOnly)

        return [permission() for permission in permission_classes]