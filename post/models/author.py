from django.db import models


class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Name'
    )
    surname = models.CharField(
        max_length=50,
        verbose_name='Surname'
    )

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        # ordering = ('uuid',)
