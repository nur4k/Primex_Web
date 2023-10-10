from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import UserManager


class User(AbstractUser):
    user_choices = (
    ('Bayer', ('Байер')),
    ('Client', ('Клиент'))
)
    email = None
    username = models.CharField(verbose_name='ФИО', max_length=155, unique=True)
    role = models.CharField(verbose_name='Роль', max_length=30, choices=user_choices, default=user_choices[1])
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=30, unique=True)
    address_delivery = models.CharField(verbose_name='Адресс доставки', max_length=155)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.username} -- {self.role}"
