from lib.base_model import BaseModel
from django.db import models


class Location(BaseModel):
    city = models.CharField(max_length=34)
    lat_long = models.JSONField()


