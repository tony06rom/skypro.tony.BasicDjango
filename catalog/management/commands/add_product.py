from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = "Add products to database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        call_command("loaddata", "./data/product_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully added products"))
