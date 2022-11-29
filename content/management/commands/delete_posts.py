from django.core.management.base import BaseCommand

from content.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        posts = Post.objects.all()

        for i in posts:
            i.delete()

        print('All Post Deleted')