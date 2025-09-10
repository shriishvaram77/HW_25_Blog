from django.core.management.base import BaseCommand
from django.core.management import call_command

from blog.models import Blogpost


class Command(BaseCommand):
    help = 'Add blogpost to the database from fixture'

    def handle(self, *args, **options):

        # Удаляем существующие записи
        Blogpost.objects.all().delete()

        # Остальной код команды
        call_command('loaddata', 'blog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
