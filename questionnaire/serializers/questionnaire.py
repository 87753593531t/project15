from rest_framework import serializers

from questionnaire.models import Questionnaire, Answer, Question
from .question import QuestionSerializer
from .answer import AnswerTextSerializer


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'uuid',
            'title',
            'description',
            'start_date',
            'end_date'
        )
        read_only_fields = ('created_at', 'updated_at')
        extra_fields = {
            'start_date': {'write_only': True}
        }

    def _get_answers(self, question_id):
        answers = AnswerTextSerializer(Answer.objects.filter(question_id=question_id), many=True).data
        return answers

    def add_questions(self, questionnaire_id):
        questions = Question.objects.filter(questionnaire_id=questionnaire_id)
        questions = QuestionSerializer(questions, many=True).data
        for question in questions:
            question['answers'] = self._get_answers(question['uuid'])
        return questions
