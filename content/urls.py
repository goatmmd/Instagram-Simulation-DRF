from django.urls import path

from content.views import TagListAPIView, PostDetailAPIView, UserPostRetrieveAPIView, UserPostListAPIView, \
    UserPostReadOnlyViewSet, TagDetailAPIView

user_post_detail = UserPostReadOnlyViewSet.as_view({'get': 'retrieve'})
user_post_list = UserPostReadOnlyViewSet.as_view({'get': 'list'})
user_post_like_list = UserPostReadOnlyViewSet.as_view({'get': 'get_like_list'})

urlpatterns = [
    path('tag/list/', TagListAPIView.as_view(), name='tag-lists'),
    path('tag/<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
    path('post/<int:pk>', PostDetailAPIView.as_view(), name='post-detail'),
    path('user/<str:username>/posts/', user_post_list, name='user-posts-list'),
    path('user/<str:username>/posts/<int:pk>/', user_post_detail, name='user-posts-detail'),
    path('user/<str:username>/posts/<int:pk>/get_like_list', user_post_like_list, name='user_post_like_list')
]
