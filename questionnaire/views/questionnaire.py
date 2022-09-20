from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.exceptions import ValidationError

from questionnaire.models import Questionnaire, Question, Answer
from questionnaire.serializers import QuestionnaireSerializer


class QuestionnaireViewSet(APIView):
    queryset = Questionnaire.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = QuestionnaireSerializer

    def get(self, request, *args, **kwargs):

        if 'uuid' in kwargs.keys():
            serializer = self.serializer_class(self.queryset.get(pk=kwargs['uuid']))
            response = serializer.data
            response['questions'] = serializer.add_questions(response['uuid'])
        else:
            response = self.serializer_class(self.queryset.all(), many=True).data

        return Response(data=response, status=status.HTTP_200_OK)