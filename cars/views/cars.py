from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django_filters import rest_framework as filters

from cars.models import Car
from cars.permissions import CarOwnerOrReadOnly
from cars.serializers import (
    CarAttachmentsUpdateSerializer,
    CarAttachmentDeleteSerializer,
    CarCreateSerializer,
    CarAttachmentCreateSerializer,
    CarListSerializer,
    CarSerializer,
    CarAttachmentSerializer
)


class CarViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = CarSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ]

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [CarOwnerOrReadOnly, ]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes.append(CarOwnerOrReadOnly)
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser, ]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = CarCreateSerializer

        if self.action == 'create':
            serializer_class = CarCreateSerializer
        elif self.action == 'update_attachments':
            serializer_class = CarAttachmentSerializer
        elif self.action == 'delete_attachments':
            serializer_class = CarAttachmentDeleteSerializer
        elif self.action == 'list':
            serializer_class = CarListSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = self.serializer_class(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_attachments(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.update_attachments()
        serializer.save()
        return Response(serializer.data)

    def get_cars(self):
        owner = self.request.user

        try:
            instance = Car.objects.filter(owner=owner)
            return instance
        except:
            raise Http404

    def get_object(self):
        uuid = self.kwargs['pk']
        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404

    def delete_attachments(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.delete_attachments()
        return Response(data={'detail': 'all deleted'},
                        status=status.HTTP_204_NO_CONTENT)
