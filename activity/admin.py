from django.contrib import admin
from django.contrib.admin import register

from activity.models import Comment, Like

@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass