from django.contrib import admin
from django.contrib.admin import register

from location.models import Location


# Register your models here.

@register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
