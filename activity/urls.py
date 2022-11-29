from django.urls import path

from activity.views import CommentListCreateAPIView, CommentRetrieveAPIView, CommentDestroyAPIView

urlpatterns = [
    path('comment/create/', CommentListCreateAPIView.as_view(), name='comment-create'),
    path('comment/retrieve/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-retrieve'),
    path('comment/delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment-delete'),
]
