from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
from relation.models import Relation


class RelationExists(BasePermission):
    message = "You should follow the user for see the posts"

    def has_permission(self, request, view):
        return Relation.objects.filter(
            from_user=request.user, to_user__username=view.kwargs['username']
        ).exists() | bool(request.user.username == view.kwargs['username'])


class HasPostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return Relation.objects.filter(
            from_user=request.user, to_user=obj.user
        ).exists() | bool(request.user == obj.user)
