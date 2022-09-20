from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .question import QuestionUUIDSerializer
from questionnaire.models import (
    Questionnaire,
    Question,
    Answer,
    UserQuestionnaire,
    UserAnswer
)


class UserQuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionUUIDSerializer(required=False, many=True)

    class Meta:
        model = UserQuestionnaire
        fields = (
            'questionnaire',
            'questions',
        )

    def validate(self, attrs):
        attrs['right_answers'] = 0
        attrs['wrong_answers'] = 0
        attrs['not_answered'] = 0
        return attrs

    def create(self, validated_data):
        right_answers = 0
        wrong_answers = 0
        not_answered = 0

        questions = validated_data.pop('questions', None)
        questionnaire = Questionnaire.objects.get(pk=validated_data['questionnaire'].uuid)
        true_questionnaire = list(questionnaire.get_question_order())

        instance = super().create(validated_data)

        if questions:
            for question in questions:
                answer = Answer.objects.get(pk=question['answer'])
                question_obj = Question.objects.get(pk=question['uuid'])
                true_questionnaire.remove(question['uuid'])
                if answer.right:
                    right_answers += 1
                    UserAnswer.objects.create(
                        right=True,
                        not_answered=False,
                        question=question_obj,
                        user_questionnaire=instance
                    )
                else:
                    wrong_answers += 1
                    UserAnswer.objects.create(
                        right=False,
                        not_answered=False,
                        question=question_obj,
                        user_questionnaire=instance
                    )

        if len(true_questionnaire) > 0:
            for question_id in true_questionnaire:
                question_obj = Question.objects.get(pk=question_id)
                UserAnswer.objects.create(
                    right=False,
                    not_answered=True,
                    question=question_obj,
                    user_questionnaire=instance
                )
                not_answered += 1

        instance.not_answered = not_answered
        instance.right_answers = right_answers
        instance.wrong_answers = wrong_answers
        instance.save()

        return instance
