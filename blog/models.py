from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок", help_text="Заголовок")
    content = models.TextField(blank=True, null=True, verbose_name="Содержимое", help_text="Содержимое")
    image = models.ImageField(upload_to="blog/images", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    sign = models.BooleanField(verbose_name="Признак публикации")
    views_cnt = models.IntegerField(default="0", verbose_name="Количество просмотров")

    def __str__(self):
        return f"Пост:{self.title} | Дата: {self.created_at} | Просмотров: {self.views_cnt}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title", "created_at", "views_cnt"]
