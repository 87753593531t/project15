from django.db import models

from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Car(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=300,
        verbose_name='Имя автомобиля'
    )
    model = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Модель'
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        related_name='cars'
    )
    date = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name='Дата'
    )

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        order_with_respect_to = 'owner'


class CarAttachment(AbstractUUID,AbstractTimeTracker):
    cars = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='Автомобиль',
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to='cars/',
        verbose_name='Вложения'
    )

    class Meta:
        verbose_name = 'Вложения автомобиля'
        verbose_name_plural = 'Вложение автомобилей'
        order_with_respect_to = 'cars'
