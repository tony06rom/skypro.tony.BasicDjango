from django.db import models

from config import settings


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Внесите название категории")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Внесите описание категории"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Внесите название продукта")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Внесите описание продукта"
    )
    image = models.ImageField(upload_to="product/images", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
        max_length=150,
        verbose_name="Категория",
        help_text="Внесите название категории продукта",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
        verbose_name="Автор",
    )

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "created_at"]
        permissions = [
            ("can_add_product", "Добавление продуктов"),
            ("can_change_product", "Изменение продуктов"),
            ("can_unpublish_product", "Отмена публикации продуктов"),
            ("can_view_unpublished", "Просмотр неопубликованных товаров"),
            ("can_delete_product", "Удаление продуктов"),
        ]

    def can_publish(self, user):
        return user.has_perm("catalog.can_unpublish_product") or user == self.owner


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=30, verbose_name="Телефон")
    message = models.TextField(max_length=300, verbose_name="Сообщение")

    def __str__(self) -> str:
        return f"Имя: {self.name} | Телефон: {self.phone}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
