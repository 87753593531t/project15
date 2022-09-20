from rest_framework import serializers

from printers.models import Printer, PrinterAttachment
from users.serializers import UserSerializer


class PrinterAttachmentSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = PrinterAttachment
        fields = (
            'uuid',
            'file'
        )
        read_only_fields = ('created_at', 'updated_at')


class PrinterAttachmentCreateSerializer(serializers.Serializer):
    uuid = serializers.PrimaryKeyRelatedField(queryset=PrinterAttachment.objects.all)


class PrinterSerializer(serializers.ModelSerializer):
    owner = UserSerializer

    class Meta:
        model = Printer
        fields = (
            'uuid',
            'title',
            'model',
            'owner',
            'attachments'
        )
        read_only_fieds = ('created_at', 'updated_at')


class PrinterCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    attachments = PrinterAttachmentCreateSerializer(required=False, many=True)

    class Meta:
        model = Printer
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
                attachment.printers = instance
                attachment.save(update_fields=['printers'])
        return instance


class PrinterListSerializer(serializers.ModelSerializer):
    owner = UserSerializer

    class Meta:
        model = Printer
        fields = (
            'uuid',
            'title',
            'model',
            'owner',
            'attachments'
        )
        read_only_fields = ('created_at', 'updated_at')


class PrinterAttachmetUpdateSerializer(serializers.Serializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Printer
        fields = (
            'title',
            'model'
        )

    def update_attachments(self):
        request = self.context['request']
        attachments = request.data['attachments']
        queryset = PrinterAttachment.objects.all()
        for attachment_data in attachments:
            instance = queryset.get(pk=attachment_data['uuid'])
            instance.update()


class PrinterAttachmentDeleteSerializer(serializers.Serializer):
    attachments = PrinterAttachmentCreateSerializer

    class Meta:
        fields = (
            'attachments'
        )

    def delete_attachments(self):
        request = self.context['request']
        attachments = request.data['attachments']
        queryset = PrinterAttachment.objects.all()
        for attachment_data in attachments:
            instance = queryset.get(pk=attachment_data['uuid'])
            instance.delete()
