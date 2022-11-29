from django.core.management.base import BaseCommand

from content.models import Tag


class Command(BaseCommand):

    def handle(self, *args, **options):
        tags = Tag.objects.all()

        deleted_tags = list()
        for tag in tags:
            tag.delete()
            deleted_tags.append(tag)

        print(f'{len(deleted_tags)} tags deleted from database')
