# from rest_framework import serializers
# from rest_framework.validators import ValidationError
#
# from post.models import News, Author
# from post.serializers import PostSerializer, PostCreateSerializer
#
#
# class NewsSerializer(serializers.ModelSerializer):
#     author = PostSerializer()
#
#     class Meta:
#         model = News
#         fields = (
#             'uuid',
#             'title',
#             'text',
#             'author'
#         )
#
#
# class NewsCreateSerializer(serializers.ModelSerializer):
#     author = PostSerializer()
#
#     class Meta:
#         model = News
#         fields = (
#             'title',
#             'text',
#             'author'
#         )
#         read_only_fields = ('uuid', )
#
#     def create(self, validated_data):
#         author = validated_data['author']
#         author_data = {}
#         author_data['name'] = author['name']
#         author_data['surname'] = author['surname']
#         if author_data:
#             new_author = PostCreateSerializer(data=author_data)
#             new_author.is_valid(raise_exception=True)
#             new_author.save()
#             validated_data['author'] = new_author.instance
#         return super().create(validated_data)
#
#
# class NewsUpdateSerializer(serializers.ModelSerializer):
#     author = PostCreateSerializer(required=False)
#
#     class Meta:
#         model = News
#         fields = (
#             'title',
#             'text',
#             'author'
#         )
#         read_only_fields = ('uuid', )
#
#     def validate(self, attrs):
#
#         if 'author' in attrs:
#             new_author_data = attrs['author']
#             if 'name' not in new_author_data.keys() and \
#                     'surname' not in new_author_data.keys():
#                 raise ValidationError('Something wrong with author field info!')
#
#             author = Author.objects.filter(id=self.context['uuid']).first()
#             if author:
#                 attrs['author'] = author
#                 attrs['new_author_data'] = dict(new_author_data)
#
#         return attrs
#
#     def update(self, instance, validated_data):
#         author = Author.objects.filter(id=self.context['uuid']).first()
#         if 'new_author_data' in validated_data.keys():
#             new_author_data = self.validated_data['new_author_data']
#             updated_author = PostCreateSerializer(author)
#             updated_author.update(author, new_author_data)
#             del validated_data['author']
#         return super().update(instance, validated_data)