from django.contrib import admin
from django.contrib.admin import register

from relation.models import Relation


# Register your models here.
@register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass
