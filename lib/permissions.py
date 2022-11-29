from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
from relation.models import Relation


class RelationExists(BasePermission):
    message = "You should follow the user for see posts"

    def has_permission(self, request, view):
        user = User.objects.filter(username=view.kwargs['username']).first()
        if user:
            return Relation.objects.filter(
                from_user=request.user, to_user=user
            ).exists() | bool(request.user == user)
        return False


class HasPostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return Relation.objects.filter(
            from_user=request.user, to_user=obj.user
        ).exists() | bool(request.user == obj.user)
