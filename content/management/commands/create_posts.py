import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from content.models import Post
from location.models import Location

CAPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' \
          'dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex '\
          'ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu ' \
          'fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt ' \
          'mollit anim id est laborum. '


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--length', type=int)

    def handle(self, *args, **options):
        users = User.objects.all()
        location = Location.objects.all()

        created_posts = []
        for i in range(options['length']):
            Post.objects.create(
                caption=CAPTION, user=random.choice(users), location=random.choice(location)
            )
            created_posts.append(i)
        print(f"{len(created_posts)} post has initiated")
