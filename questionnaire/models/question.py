from django.db import models

from .questionnaire import Questionnaire
from utils.models import AbstractUUID, AbstractTimeTracker


class Question(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=255,
        verbose_name='Название вопроса'
    )
    text = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Описание вопроса'
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        on_delete=models.CASCADE,
        verbose_name='Номер вопросника'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        order_with_respect_to = 'questionnaire'

    def __str__(self):
        return self.title
