from django.contrib.auth.models import User
from django.db import models

from lib.base_model import BaseModel
from location.models import Location


class Post(models.Model):
    caption = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='posts', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} --> {self.id}"


class PostMedia(BaseModel):
    IMAGE = 1
    VIDEO = 2

    TYPE_CHOICES = (
        (IMAGE, 'Img'),
        (VIDEO, 'Vid'),
    )

    media_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=IMAGE)
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_file = models.FileField(upload_to='content\\media\\', )

    def __str__(self):
        return f"{self.post} uploaded {self.get_media_type_display()}"


class Tag(BaseModel):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name='tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} --> {self.tag}"
