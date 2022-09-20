# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
#
# from post.models import News
# from post.serializers import (
#     NewsSerializer,
#     NewsCreateSerializer,
#     NewsUpdateSerializer
# )
#
#
# class NewsViewSet(APIView):
#     serializer_class = NewsSerializer
#     permission_classes = [AllowAny, ]
#     queryset = News.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         serializer = NewsCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(News.objects.all(), many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         uuid = request.query_params.get('uuid', False)
#         news = News.objects.filter(pk=uuid).first()
#         serializer = NewsUpdateSerializer(data=request.data, context={'uuid': news.author_id})
#         serializer.is_valid(raise_exception=True)
#         serializer.update(news, serializer.data)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)