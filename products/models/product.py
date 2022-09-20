from django.db import models

from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Product(AbstractUUID, AbstractTimeTracker):
    name = models.CharField(
        max_length=255,
        verbose_name='Наименование продукта'
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Описание продукта'
    )
    cost = models.IntegerField(
        default=0,
        verbose_name='Стоимость продукта'
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Владелец продукта',
        related_name='products'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        order_with_respect_to = 'owner'


class ProductAttachment(AbstractUUID, AbstractTimeTracker):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='Товар',
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to='products/',
        verbose_name='Вложения'
    )

    class Meta:
        verbose_name = 'Вложение товара'
        verbose_name_plural = 'Вложения товаров'
        order_with_respect_to = 'product'