from django.db import models


class About_As(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class FeedBack(models.Model):
    theme_choices = (
        ('Cargo', ('Карго')),
        ('Forwarding', ('Пересылка')),
        )

    fio = models.CharField(verbose_name='ФИО', max_length=155)
    email = models.EmailField(verbose_name='Email', max_length=155, null=True, blank=True)
    number = models.IntegerField(verbose_name='Номер телефона', null=True, blank=True)
    theme = models.CharField(verbose_name='Выборка', choices=theme_choices, max_length=10, default=theme_choices[0], null=True, blank=True)
    title = models.CharField(verbose_name='Тема', max_length=500, help_text='Макс. символов 500', null=True, blank=True)
    description = models.CharField(verbose_name='Обращение', max_length=500, help_text='Макс. символов 500', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.fio} -- {self.title}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
