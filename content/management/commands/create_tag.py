import random

from django.core.management.base import BaseCommand
from content.models import Tag


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--length', type=int)

    def handle(self, *args, **options):
        tags = ['Php', 'Python', 'Programming', 'Django', 'Flask', 'Java']

        for i in range(options['length']):
            Tag.objects.create(
                title=random.choice(tags) + '-' + str(i)
            )
        print('tags Created')
