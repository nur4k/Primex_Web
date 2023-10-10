from django.db import models


class FAQ(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'F.A.Q'
        verbose_name_plural = 'F.A.Q'

