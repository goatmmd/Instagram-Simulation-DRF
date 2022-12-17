from rest_framework.permissions import BasePermission
from relation.models import Relation


class IsOwnComment(BasePermission):
    message = "Access Denied"

    def has_object_permission(self, request, view, obj):
        relation_exists = Relation.objects.filter(from_user=request.user, to_user=obj.user).first()
        return bool(relation_exists) | bool(obj.user == request.user)
