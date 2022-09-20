from rest_framework.serializers import ModelSerializer

from questionnaire.models import Answer


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'uuid',
            'text',
            'right',
            'question'
        )
        read_only_fields = ('created_at', 'updated_at')


class AnswerTextSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text', )
