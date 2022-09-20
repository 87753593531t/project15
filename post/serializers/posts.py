from rest_framework import serializers

from post.models import Post
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'uuid',
            'name',
            'author',
            'content'
        )

class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'name',
            'author',
            'content'
        )

    # def create(self, validated_data):
    #
    #     if new_author_data:
    #         new_author = PostCreateSerializer(data=new_author_data)
    #         new_author.is_valid(raise_exception=True)
    #         new_author.save()
    #         validated_data['author'] = new_author.instance
    #     return super().create(validated_data)


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'name',
            'author',
            'content'
        )

        read_only_fields = ('created_at', 'updated_at')


class PostUpdateSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = (
            'name',
            'content'
        )

    def update(self, instance, validated_data):
        if 'author' in validated_data.keys():
            author = Post.objects.filter(id=instance.author_id).first()
            author_serializer = PostCreateSerializer(author)
            author_serializer.update(author, dict(validated_data['author']))
            del validated_data['author']
        return super().update(instance, validated_data)

