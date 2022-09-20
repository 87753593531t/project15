from django.db import models

from .userquestionnaire import UserQuestionnaire
from .question import Question
from utils.models import AbstractUUID, AbstractTimeTracker


class UserAnswer(AbstractUUID, AbstractTimeTracker):
    right = models.BooleanField(
        default=False,
        verbose_name='Правильный ответ пользователя'
    )
    not_answered = models.BooleanField(
        default=False,
        verbose_name='Не отвеченный'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    user_questionnaire = models.ForeignKey(
        UserQuestionnaire,
        on_delete=models.CASCADE,
        verbose_name='Вариант пользователя'
    )

    class Meta:
        verbose_name = 'UserAnswer'
        verbose_name_plural = 'UserAnswers'
