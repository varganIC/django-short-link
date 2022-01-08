from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    lohg_link = models.URLField("Длинная ссылка", max_length=250, default='', unique=True)
    short = models.SlugField("Сокращенное слово", max_length=10, default='', unique=True,  primary_key=True)
    short_link = models.URLField("Сокращенная ссылка", max_length=20, default='', unique=False)

    def get_absolute_url(self):
        return reverse('short-page')

    def __str__(self):
        return self.lohg_link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
