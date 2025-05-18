from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    help = "Add categories to database"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command("loaddata", "/data/category_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully added categories"))
