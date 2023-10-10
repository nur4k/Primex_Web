from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=155)
    image = models.ImageField(verbose_name='Фото', upload_to='news/image')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_created=True)
    views = models.IntegerField(verbose_name='Кол-во просмотров')

    def __str__(self) -> str:
        return f"{self.title} -- {self.created_at}"
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
