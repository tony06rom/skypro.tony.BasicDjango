from django.core.management import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="moder_coder@example.com")
        user.set_password("12345678")
        user.is_active = True
        user.save()
