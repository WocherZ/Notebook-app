from django.urls import reverse
from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    name = models.CharField(verbose_name="Наименование заметки",
                            max_length=128,
                            null=False)
    text = models.TextField(verbose_name="Текст заметки",
                            null=False)
    date_published = models.DateTimeField(verbose_name="Дата публикации",
                                          default=timezone.now,
                                          null=False)
    slug = models.SlugField(verbose_name="Уникальная ссылка",
                            max_length=148,
                            unique=True)


    def get_absolute_url(self):
        return reverse('note', kwargs={'note_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Список заметок"
