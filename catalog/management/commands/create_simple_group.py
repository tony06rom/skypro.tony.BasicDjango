from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = "Creates simple group with permissions"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Пользователи")

        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(
            content_type=content_type, codename__in=["can_add_product", "can_view_product"]
        )
        group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS("Группа пользователей создана"))
