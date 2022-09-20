from django.db import models

from .question import Question
from utils.models import AbstractUUID, AbstractTimeTracker


class Answer(AbstractUUID, AbstractTimeTracker):
    text = models.CharField(
        max_length=1000,
        verbose_name='Ответ'
    )
    right = models.BooleanField(
        default=False,
        verbose_name='Правильно'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Номер вопроса'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        order_with_respect_to = 'question'

    def __str__(self):
        return self.text
