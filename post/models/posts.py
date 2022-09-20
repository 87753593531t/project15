from django.db import models

# from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Post(AbstractUUID, AbstractTimeTracker):
    name = models.CharField(
        max_length=100,
        default=''
    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    content = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('uuid',)

