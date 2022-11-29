from django.contrib import admin
from django.contrib.admin import register

from content.models import Post, PostMedia, Tag, PostTag


# Register your models here.

class PostMediaTabularInline(admin.TabularInline):
    model = PostMedia


class PostTagTabularInline(admin.TabularInline):
    model = PostTag


@register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostMediaTabularInline, PostTagTabularInline]


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    pass


admin.register(Post, PostAdmin)
admin.register(Tag, TagAdmin)
admin.register(PostTag, PostTagAdmin)
