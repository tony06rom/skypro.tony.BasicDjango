from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "sign",
    )
    list_filter = ("created_at", "views_cnt",)
    search_fields = (
        "title",
        "content",
    )
