from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from activity.models import Comment, Like
from activity.permissions import IsOwnComment
from activity.serializers import CommentCreateSerializer, CommentListSerializer, PostLikeSerializer
from lib.permissions import HasPostPermission


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return self.serializer_class


class CommentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated, IsOwnComment)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return self.serializer_class

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(user=self.request.user)


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()


class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated, HasPostPermission]
