from django.contrib.auth.models import User
from django.db import models

from content.models import Post
from lib.base_model import BaseModel


class Comment(BaseModel):
    text = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text


class Like(BaseModel):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} >> {self.post}"
