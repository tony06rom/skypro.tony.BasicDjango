from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=30, verbose_name="Телефон", blank=True, null=True, help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to="data/media/users/avatars/", verbose_name="Аватар", blank=True, null=True, help_text="Загрузите своё аватар")
    country = models.CharField(max_length=50, verbose_name="Страна")
    token = models.CharField(max_length=100, verbose_name="Токен", blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return {self.email}

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
