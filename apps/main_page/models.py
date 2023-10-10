from django.db import models


class MainPage(models.Model):
    title = models.CharField(verbose_name='Название', max_length=155)
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'
