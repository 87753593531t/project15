from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from questionnaire.models import Answer
from questionnaire.serializers import AnswerSerializer


class AnswerVewSet(ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = AnswerSerializer
