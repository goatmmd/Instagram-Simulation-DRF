from django.contrib.auth.models import User
from django.db import models

from lib.base_model import BaseModel


class Relation(BaseModel):
    from_user = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_user} >> {self.to_user}"
