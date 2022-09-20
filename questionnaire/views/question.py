from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from questionnaire.models import Question
from questionnaire.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = QuestionSerializer
