from django.db import models


class Service(models.Model):
    title = models.CharField(verbose_name='Название', max_length=155)
    description = models.TextField(verbose_name='Описание')
    icon = models.ImageField(verbose_name='Иконка', upload_to='services/icon')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
