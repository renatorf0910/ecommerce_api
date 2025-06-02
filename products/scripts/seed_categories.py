from django.core.management.base import BaseCommand
from django.utils.text import slugify

from products.contants import CATEGORY_CHOICES
from products.models import Category

class Command(BaseCommand):
    help = 'Popula categorias padrão'

    def handle(self, *args, **kwargs):
        for key, label in CATEGORY_CHOICES:
            obj, created = Category.objects.get_or_create(
                name=label,
                defaults={"slug": slugify(label)}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Categoria criada: {label}'))
            else:
                self.stdout.write(f'Categoria já existe: {label}')
