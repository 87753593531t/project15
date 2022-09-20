from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker


class Questionnaire(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Описание вопросника'
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Вопросник'
        verbose_name_plural = 'Вопросники'

    def __str__(self):
        return str(self.uuid)
