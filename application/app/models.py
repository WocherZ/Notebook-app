from django.db import models


# Create your models here.
class Note(models.Model):
    name = models.CharField(verbose_name="Наименование заметки",
                            max_length=128,
                            null=False)
    text = models.TextField(verbose_name="Текст заметки",
                            null=False)
    date_published = models.DateTimeField(verbose_name="Дата публикации",
                                          auto_now=True,
                                          null=False)

