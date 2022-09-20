from rest_framework import serializers

from cars.models import Car, CarAttachment
from users.serializers import UserSerializer


class CarAttachmentSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = CarAttachment
        fields = (
            'uuid',
            'file'
        )
        read_only_fields = ('created_at', 'updated_at')


class CarAttachmentCreateSerializer(serializers.Serializer):
    uuid = serializers.PrimaryKeyRelatedField(queryset=CarAttachment.objects.all())


class CarSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault)
    owner = UserSerializer()

    class Meta:
        model = Car
        fields = (
            'uuid',
            'title',
            'model',
            'owner',
            'attachments'
        )
        read_only_fields = ('created_at', 'updated_at')


class CarCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    attachments = CarAttachmentCreateSerializer(required=False, many=True)

    class Meta:
        model = Car
        fields = (
            'uuid',
            'title',
            'model',
            'owner',
            'attachments'
        )
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        attachments = validated_data.pop('attachments', None)

        instance = super().create(validated_data)

        if attachments:
            for attachment_data in attachments:
                attachment = attachment_data['uuid']
                attachment.cars = instance
                attachment.save(update_fields=['cars'])

        return instance


class CarListSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Car
        fields = (
            'uuid',
            'title',
            'model',
            'owner',
            'attachments'
        )
        read_only_fields = ('created_at', 'updated_at')


class CarAttachmentsUpdateSerializer(serializers.Serializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = (
            'title',
            'model'
        )

        def update_attachments(self):
            request = self.context['request']
            attachments =request.data['attachments']
            queryset = CarAttachment.objects.all()
            for attachment_data in attachments:
                instance = queryset.get(pk=attachment_data['uuid'])
                instance.update()


class CarAttachmentDeleteSerializer(serializers.Serializer):
    attachments = CarAttachmentCreateSerializer()

    class Meta:
        fields = (
            'attachments',
        )

    def delete_attachments(self):
        request = self.context['request']
        attachments = request.data['attachments']
        queryset = CarAttachment.objects.all()
        for attachment_data in attachments:
            instance = queryset.get(pk=attachment_data['uuid'])
            instance.delete()
