from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'created_at',
            'updated_at',
            'phone',
            'first_name',
            'avatar',
            'is_staff',
            'is_active',
            # 'Email'
        )
