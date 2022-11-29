from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from activity.models import Comment, Like


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'post', 'reply_to')

    def validate_reply_to(self, attr):
        if attr is None:
            return attr
        elif attr.reply_to is not None:
            raise ValidationError("You can't reply to a reply recursively")
        else:
            return attr


class CommentRepliesListSerialize(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    # reply_to = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'user', 'replies')

    def get_replies(self, obj):
        serializer = CommentRepliesListSerialize(obj.replies.all()[:10], many=True)
        return serializer.data


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('post', )