from django.db import models

from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Printer(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(
        max_length=500,
        verbose_name='Имя принтера'
    )

    model = models.CharField(
        max_length=1000,
        verbose_name='Модель'
    )

    date = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name='Дата'
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        related_name='printers'
    )

    class Meta:
        verbose_name = 'Принтер',
        verbose_name_plural = 'Принтеры',
        order_with_respect_to = 'owner'


class PrinterAttachment(AbstractUUID,AbstractTimeTracker):
    printers = models.ForeignKey(
        Printer,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='Принтер',
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to='printers',
        verbose_name='Влажения'
    )

    class Meta:
        verbose_name = 'Влажения принтера',
        verbose_name_plural = 'Влажение принтеров',
        order_with_respect_to = 'printers'
