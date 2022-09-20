# from django.db import models
#
#
# class News(models.Model):
#     title = models.CharField(
#         max_length=100,
#         verbose_name='Title'
#     )
#     text = models.CharField(
#         max_length=100,
#         verbose_name='Text'
#     )
#     author = models.ForeignKey(
#         'post.Author',
#         on_delete=models.CASCADE,
#         verbose_name='Author'
#     )
#
#     class Meta:
#         verbose_name = 'News'
#         verbose_name_plural = 'News'
#         # ordering = ('id', )