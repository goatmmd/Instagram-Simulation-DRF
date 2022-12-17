from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView

from activity.serializers import LikeSerializer
from content.models import Tag, Post
from content.serializers import TagListSerializer, PostDetailSerializer, TagDetailSerializer
from lib.pagination import SmallPageNumberPagination
from lib.permissions import RelationExists
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.generics import ListAPIView


# class TagListAPIView(ListCreateAPIView):
#     serializer_class = TagListSerializer
#     queryset = Tag.objects.all()
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = SmallPageNumberPagination

class TagListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer

    # region customize get(self, *args, **kwargs) before use instead ListAPIView meanwhile for post method
    # def get(self, *args, **kwargs):
    #     print(self.request.user)
    #     tags = Tag.objects.all()
    #
    #     serializer = TagListSerializer(tags, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     serializer = TagListSerializer(data=self.request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


class TagDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        instance = get_object_or_404(Tag, **{'pk': kwargs['pk']})

        serializer = TagDetailSerializer(instance)
        return Response(serializer.data)


# class PostDetailAPIView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     # authentication_classes = (SessionAuthentication, JWTAuthentication) if settings.DEBUG else (JWTAuthentication,)
#
#     def get(self, *args, **kwargs):
#         post = get_object_or_404(Post, **{'pk': kwargs['pk']})
#         serializer = PostDetailSerializer(post)
#         return Response(serializer.data)


class PostDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Post, **{'pk': kwargs['pk']})
        serializer = PostDetailSerializer(instance)
        return Response(serializer.data)


class UserPostListAPIView(ListAPIView):
    lookup_url_kwarg = 'user_id'
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated, RelationExists]

    def get_queryset(self):
        qs = Post.objects.filter(user_id=self.kwargs[self.lookup_url_kwarg])
        return qs


class UserPostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticated, RelationExists]

    # def get_queryset(self):
    #     qs = Post.objects.filter(user_id=self.kwargs[self.lookup_url_kwarg])
    #     return qs
    #

    # def post(self):
    #     self.get_object()


class UserPostReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_url_kwarg = 'pk'
    pagination_class = SmallPageNumberPagination
    permission_classes = [IsAuthenticated, RelationExists]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__username=self.kwargs['username'])

    def get_serializer_class(self):
        if self.action == 'get_like_list':
            return LikeSerializer
        return self.serializer_class

    @action(methods=["GET"], detail=True)
    def get_like_list(self, request, *args, **kwargs):
        post = self.get_object()
        queryset = post.likes.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
