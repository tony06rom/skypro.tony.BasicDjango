from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id","name",)
    list_filter = ("name",)
    search_fields = ("name","description",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name","price","category",)
    list_filter = ("category",)
    search_fields = ("name","description",)
