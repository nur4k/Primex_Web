from django.db import models


class Partner(models.Model):
    logo = models.ImageField(verbose_name='Логотип', upload_to='partners/logo')
    address = models.CharField(verbose_name='Адрес', max_length=155)
    contacts = models.IntegerField(verbose_name='Контакты')

    def __str__(self) -> str:
        return self.address
    
    class Meta:
        verbose_name = 'Парнтер'
        verbose_name_plural = 'Парнтеры'
