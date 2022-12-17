from django.contrib.auth.models import User
from rest_framework import serializers

from activity.serializers import CommentListSerializer
# from activity.serializers import CommentListSerializer
from content.models import Tag, Post, PostMedia, PostTag
from location.serializers import LocationSerializer


class TagListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ('id', 'title')


# region normal serializer without specific any options
# class TagListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#
#     def create(self, validated_data):
#         instance = Tag.objects.create(**validated_data)
#         return instance


class TagDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ('id', 'title', 'posts')

    def get_posts(self, obj):
        return obj.posts.count()


# class PostDetailSerializer(serializers.ModelSerializer):
#     user = serializers.CharField(source='user.username')
#     location = LocationDetailSerializer()
#     comments = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Post
#         fields = ('id', 'caption', 'user', 'location', 'comments')
#
#     def get_comments(self, obj):
#         serializer = CommentListSerializer(obj.comments.all(), many=True)
#         return serializer.data


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('id', 'media_type', 'media_file')


class PostTagSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source='tag.title')

    class Meta:
        model = PostTag
        fields = ('tag',)


class PostDetailSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    user = serializers.CharField(source='user.username')
    location = LocationSerializer()
    media = PostMediaSerializer(many=True)
    tags = PostTagSerializer(many=True)
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'caption', 'user', 'location', 'media', 'tags', 'comments')
