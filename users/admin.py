from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "first_name", "last_name", "is_staff")
    search_fields = ("email", "username")
    ordering = ("email",)
