from rest_framework import serializers

from questionnaire.models import Question
# from .answer import AnswerUUIDSerializer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'uuid',
            'title',
            'text',
            'questionnaire'
        )
        read_only_fileds = ('created_at', 'updated_at')


class QuestionUUIDSerializer(serializers.Serializer):
    # answer = AnswerUUIDSerializer(required=False)
    uuid = serializers.UUIDField(required=True)
    answer = serializers.UUIDField(required=False)

    class Meta:
        model = Question
        fields = ('uuid', 'answer')
