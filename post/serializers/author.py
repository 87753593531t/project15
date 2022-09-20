from rest_framework import serializers

from post.models import Author
from users.serializers import UserSerializer


class AuthorSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer()
    class Meta:
        model = Author
        fields = (
            'uuid',
            'name',
            'surname'
        )


class AuthorCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer()

    class Meta:
        model = Author
        fields = (
            'name',
            'surname'
        )
