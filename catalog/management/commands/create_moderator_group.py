from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = "Creates moderator group with permissions"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                "can_unpublish_product",
                "can_delete_product",
                "can_view_unpublished",
                "can_change_product",
                "can_update_product",
            ],
        )
        group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS("Группа модераторов создана"))
