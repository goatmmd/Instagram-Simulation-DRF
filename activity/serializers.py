from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from activity.models import Comment, Like
from rest_framework.pagination import CursorPagination


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'post', 'reply_to')

    # def validate_reply_to(self, attr):
    #     if attr is None:
    #         return attr
    #     elif attr.reply_to is not None:
    #         raise ValidationError("You can't reply to a reply recursively")
    #     else:
    #         return attr

    def validate_reply_to(self, attr):
        if attr.reply_to is not None:
            raise ValidationError("You can't reply to a reply recursively")
        return attr


class CommentRepliesListSerialize(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'reply_to')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'replies', 'post')

    def get_replies(self, obj):
        qs = obj.replies.all()

        if qs.count() > 10:
            qs = qs[:10]

        serializer = CommentRepliesListSerialize(qs, many=True)
        return serializer.data


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post',)


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Like
        fields = ("user",)
